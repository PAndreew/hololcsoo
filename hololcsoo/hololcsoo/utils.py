"""Utility functions to perform scraping"""

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.addArgument('--ignore-certificate-errors')
# options.addArgument('--incognito')
# options.addArgument('headless')
options.add_argument('--start-maximized')


def launch_broswer(start_url):
    """General function to start selenium driver"""
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(start_url)
    return driver


def scrape_auchan_categories():
    """Scrape Auchan categories and put them into a list"""
    driver = launch_broswer('https://online.auchan.hu/shop')

    time.sleep(0.5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, '_1DRX').click()
    time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, 'Tulx').click()
    time.sleep(0.2)
    driver.find_element(By.CLASS_NAME, '_23Mg').click()

    auchan_hrefs = [element.get_attribute("href") for element in driver.find_elements_by_xpath("//a[@href]")]

    return auchan_hrefs


def scrape_spar_categories():

    spar_category_dict = {}

    spar_main_page = requests.get("https://www.spar.hu/onlineshop/")

    spar_main_page_soup = BeautifulSoup(spar_main_page.content, 'html.parser')

    category_set = spar_main_page_soup.find_all("a", class_="flyout-categories__link")

    href_list = list(filter(('javascript:void(0)').__ne__, [category['href'] for category in category_set]))

    for href in href_list:
        spar_category_dict[href.split("/")[-2]] = href.split("/")[-4]

    return spar_category_dict


def scrape_spar_products(category_url):
    """Scrape SPAR product info for a given category"""
    driver = launch_broswer(category_url)

    product_list = []
    y = 500
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    while y <= total_height:
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        elements = driver.find_elements(By.CLASS_NAME, 'productBox')
        for WebElement in elements:
            element_html = WebElement.get_attribute('outerHTML')  # gives exact HTML content of the element
            element_soup = BeautifulSoup(element_html, 'html.parser')
            product_list.append(element_soup)
        time.sleep(2)

    return product_list


def scrape_auchan_products(category_url):
    """Scrape Auchan product info for a given category"""
    driver = launch_broswer(category_url)

    y = 500
    product_list = []
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    while y <= total_height:
        elements = driver.find_elements(By.CLASS_NAME, '_48TB')
        for WebElement in elements:
            element_html = WebElement.get_attribute('outerHTML')  # gives exact HTML content of the element
            element_soup = BeautifulSoup(element_html, 'html.parser')
            product_list.append(element_soup)
        y += 500
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        time.sleep(2)

    return product_list


def create_spar_product_dict(html_product_list):
    product_dict = {}
    for productBox in html_product_list:
        badge_name = productBox.find("div", class_='badgeName')
        product_name = productBox.find("a", id=lambda x: x and x.startswith('product-')).text
        product_dict[product_name] = {
            'name': product_name,
            'category': 'H3-1',
            'sold_by': 'SPAR',
            'price': productBox.find("label", class_='priceInteger').text,
            'unit_price': productBox.find("label", class_='extraInfoPrice').text,
            'is_vegan': False,
            'is_cooled': False,
            'is_local_product': False,
            'is_bio': False,
        }
        if badge_name:
            if badge_name.text.strip() == "Hűtött":
                product_dict[product_name]['is_cooled'] = True
            if badge_name.text.strip() == "Hazai Termék":
                product_dict[product_name]['is_local_product'] = True
            if badge_name.text.strip() == "BIO":
                product_dict[product_name]['is_bio'] = True

    return product_dict


def create_auchan_product_dict(html_product_list):
    product_dict = {}

    for productDiv in html_product_list:
        badge_names = [image['alt'] for image in productDiv.find_all("img", class_='_2Py5')]
        product_name = productDiv.find("a", class_='_2J-k').find("span").text
        product_dict[product_name] = {
            'name': product_name,
            'category': 'c-6537',
            'sold_by': 'Auchan',
            'price': productDiv.find("div", class_='_3vje').text,
            'unit_price': productDiv.find("div", class_='_20Mg').text,
            'is_vegan': False,
            'is_cooled': False,
            'is_local_product': False,
            'is_bio': False,
            'product_url': dict.fromkeys(filter(('javascript: void(0)').__ne__, [category['href'] for category in
                                                                                 productDiv.find_all("a",
                                                                                                     href=True)])).keys()
        }
        if badge_names:
            for badge_name in badge_names:
                if badge_name.strip() == "Hűtött termék":
                    product_dict[product_name]['is_cooled'] = True
                if badge_name.strip() == "Magyar termék":
                    product_dict[product_name]['is_local_product'] = True
                if "Hazai Termék" in badge_name.strip():
                    product_dict[product_name]['is_local_product'] = True
                if badge_name.strip() == "BIO":
                    product_dict[product_name]['is_bio'] = True

    return product_dict
