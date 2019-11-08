import json
import logging

from crawl_websummit_startups import output_filename


def analyze():
    logger = logging.getLogger('WebSummit2019StartupCrawler')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    with open(output_filename, 'r') as file:
        companies = json.loads(file.read())

    for social_platform in ["facebook", "instagram", "twitter", "crunchbase", "website", "angellist", "linkedin"]:
        companies_with_facebook = [company for company in companies if social_platform in company]
        print("With {}: {}".format(social_platform, len(companies_with_facebook)))

if __name__ == '__main__':
    analyze()
