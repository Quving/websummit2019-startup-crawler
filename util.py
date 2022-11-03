from json import JSONDecoder

from selenium import webdriver

import json

from seleniumwire.request import Request


def extract_json_from_string(text, decoder=JSONDecoder()):
    """
    Extract JSON from a string.
    """
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1


def extract_network_requests_from_driver(driver: webdriver):
    """
    Extract network requests from a Selenium driver.
    More: https://gist.github.com/lorey/079c5e178c9c9d3c30ad87df7f70491d
    """
    #
    # This small example shows you how to access JS-based requests via Selenium
    # Like this, one can access raw data for scraping,
    # for example on many JS-intensive/React-based websites
    #

    # extract requests from logs
    logs_raw = driver.get_log("performance")
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

    def log_filter(log_):
        return (
            # is an actual response
                log_["method"] == "Network.responseReceived"  # and json
                and "json" in log_["params"]["response"]["mimeType"]
        )

    for log in filter(log_filter, logs):
        request_id = log["params"]["requestId"]
        resp_url = log["params"]["response"]["url"]
        print(f"Caught {resp_url}")
        print(driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id}))


def extract_data_from_request(network_requests: list) -> list:
    def filter_request(request: Request):
        """
        Return true on requests that contain the data we want.
        """
        if not request.response:
            return False

        header_matched = request.response.headers['Content-Type'] == 'application/json; charset=UTF-8'
        method_matched = request.method == 'POST'

        return header_matched and method_matched

    request_filtered = list(filter(filter_request, network_requests))

    data = []

    for request in request_filtered:
        from seleniumwire.utils import decode

        response = request.response
        body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))

        # Decode bytes to string
        results = json.loads(body.decode('utf-8')).get('results', [])
        for result in results:
            data.extend(result['hits'])

    return data
