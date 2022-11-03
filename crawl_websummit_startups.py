import json
import logging
import pickle
import time

from selenium.webdriver import DesiredCapabilities
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By

from util import extract_json_from_string, extract_network_requests_from_driver, extract_data_from_request

logger = logging.getLogger('WebSummit2019StartupCrawler')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

websummit_startup_url = 'https://websummit.com/featured-startups'
output_filename = 'websummit2022startups.json'


def crawl_startups():
    # WebDriver configuration

    driver = webdriver.Chrome(executable_path='chromedriver/chromedriver')
    driver.implicitly_wait(10)

    # Start crawling
    driver.get(websummit_startup_url)

    # Agree to cookies
    driver.find_element(
        By.CSS_SELECTOR,
        'div.civic_cookie__grid_body div[data-test-id="cookie-acceptance-btn"]'
    ).click()

    next_page_available = True
    # next_page_available = False

    # extract_network_requests_from_driver(driver)

    company_list = []
    while next_page_available:
        # Wait for the page to load and perform requests before scraping
        time.sleep(5)

        # Extract network requests
        data = extract_data_from_request(network_requests=driver.requests)

        company_list.extend(data)

        try:
            # Scroll down
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Click on next page
            btn_next_page = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Go to next page"]')
            btn_next_page.click()

        except NoSuchElementException as e:
            print("Element not found")
            next_page_available = False
        except ElementClickInterceptedException as e:
            # Usually thrown after last page is reached
            print("Last page reached")
            next_page_available = False
        except ElementNotInteractableException as e:
            print("Element not interactable")
            next_page_available = False
        except Exception as e:
            print("Unknown error: {}".format(e))

    driver.quit()

    logger.info("Export to json file.")

    # Remove duplicate dicts
    company_list = [json.loads(j) for j in set([json.dumps(d) for d in company_list])]

    with open(output_filename, 'w') as file:
        json.dump(company_list, file, indent=True)


if __name__ == '__main__':
    crawl_startups()
