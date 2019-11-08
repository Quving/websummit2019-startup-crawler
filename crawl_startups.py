import json
import logging
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

logger = logging.getLogger('WebSummit2019StartupCrawler')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

websummit_startup_url = 'https://websummit.com/featured-startups'
output_filename = 'websummit2019startups.json'

# WebDriver configuration
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Start crawling
driver.get(websummit_startup_url);

# Click on 'load-more' if possible
logger.info("Click on 'Show More' as much as possible...")
next_page_available = True
while next_page_available:
    try:
        driver.find_element_by_class_name('ais-InfiniteHits-loadMore').click()
        time.sleep(0.5)
    except NoSuchElementException:
        next_page_available = False
    except ElementNotInteractableException:
        next_page_available = False

logger.info("Start crawling startups...")
companies = []

names = driver.find_elements_by_css_selector('div.algolia-hit-box .algolia-text-block h4')
metas = driver.find_elements_by_css_selector('div.algolia-hit-box .algolia-text-block span.text-span')
logos = driver.find_elements_by_css_selector('div.algolia-hit-box .algolia-img-block img')
descriptions = driver.find_elements_by_css_selector('div.algolia-hit-box .algolia-text-block div span')
listitems = driver.find_elements_by_class_name('ais-InfiniteHits-item')

assert len(names) == len(metas) == len(logos) == len(descriptions) == len(listitems)
for name, meta, logo, description, listitem in zip(names, metas, logos, descriptions, listitems):
    driver.execute_script("arguments[0].scrollIntoView();", listitem)
    time.sleep(0.5)
    listitem.click()
    time.sleep(0.5)
    print(meta.text)
    # Crawl data metadata
    company = {
        'name': name.text,
        'description': description.text,
        'country': meta.text.split("|")[0].strip() if "|" in meta.text else "unknown",
        'sector': meta.text.split("|")[1].strip() if "|" in meta.text else "unknown",
        'logo': logo.get_attribute('src'),
        'websummit': ['2019']
    }

    # Crawl details
    socials = driver.find_elements_by_css_selector('div.modal-social-links span.m-social')
    for social in socials:
        social_type = social.get_attribute('class').split('-')[-1]
        social_url = driver.find_element_by_css_selector(
            'div.modal-social-links span.m-{} a'.format(social_type)).get_attribute('href')
        company[social_type] = social_url

    # Close popups
    driver.find_element_by_class_name('modal__close-btn').click()

    companies.append(company)
    logger.info("Companies crawled: {}".format(len(companies)))

driver.quit()

logger.info("Export to json file.")
with open(output_filename, "w") as file:
    json.dump(companies, file, indent=True)
