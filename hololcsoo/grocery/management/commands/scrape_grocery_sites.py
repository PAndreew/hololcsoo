import re
import time
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# options.addArgument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--start-maximized')


def launch_broswer(start_url):
    """General function to start selenium driver"""
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(start_url)
    return driver


def scrape_auchan_hrefs() -> list:
    """Scrape Auchan categories and put them into a list"""
    driver = launch_broswer('https://online.auchan.hu/shop')

    time.sleep(0.5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(0.3)
    # driver.find_element(By.CLASS_NAME, '_1DRX').click()
    # time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, 'Tulx').click()
    time.sleep(0.2)
    driver.find_element(By.CLASS_NAME, '_23Mg').click()

    auchan_hrefs = [element.get_attribute("href") for element in driver.find_elements(by=By.XPATH, value="//a[@href]")]

    return auchan_hrefs


def extract_auchan_categories(href_list) -> list:
    auchan_category_urls = [href for href in href_list if re.search('\\.c-.*[0-9]$', href)]
    return auchan_category_urls


class Command(BaseCommand):
    def handle(self, *args, **options):
        auchan_href_list = scrape_auchan_hrefs()
        print(extract_auchan_categories(auchan_href_list))
