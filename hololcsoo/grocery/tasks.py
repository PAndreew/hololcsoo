from __future__ import absolute_import, unicode_literals
import logging
import re
import time
import unicodedata
from celery import shared_task
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from .models import Food, Price, Category

logger = logging.getLogger(__name__)

options = webdriver.ChromeOptions()
# options.addArgument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument('--start-maximized')


# def delete_old_job_executions(max_age=604_800):
#     """Deletes all apscheduler job execution logs older than `max_age`."""
#     DjangoJobExecution.objects.delete_old_job_executions(max_age)

@shared_task
def launch_broswer(start_url):
    """General function to start selenium driver"""
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(start_url)
    return driver


@shared_task
def scrape_auchan_hrefs(driver) -> list:
    """Scrape Auchan categories and put them into a list"""
    # driver = launch_broswer('https://online.auchan.hu/shop')
    driver.get('https://online.auchan.hu/shop')
    time.sleep(0.5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, '_1DRX').click()
    time.sleep(0.3)
    driver.find_element(By.CLASS_NAME, 'Tulx').click()
    time.sleep(0.2)
    driver.find_elements(By.CLASS_NAME, '_23Mg')[1].click()

    auchan_hrefs = [element.get_attribute("href") for element in driver.find_elements(by=By.XPATH, value="//a[@href]")]

    return auchan_hrefs


@shared_task
def extract_auchan_categories(href_list) -> list:
    auchan_category_urls = [href for href in href_list if re.search('\\.c-.*[0-9]$', href)]
    return auchan_category_urls


@shared_task
def scrape_auchan_products(driver, category_url) -> list:
    """Scrape Auchan product info for a given category"""
    # driver = launch_broswer(category_url)
    driver.get(category_url)
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


@shared_task
def create_auchan_product_dict(html_product_list) -> dict:
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


@shared_task(name='run_scheduled_jobs')
def update_auchan_product_table():
    driver = launch_broswer('https://online.auchan.hu/shop')
    auchan_href_list = scrape_auchan_hrefs(driver)
    auchan_category_url_list = extract_auchan_categories(auchan_href_list)
    auchan_product_list = []
    for url in auchan_category_url_list[:2]:
        auchan_product_list.extend(scrape_auchan_products(driver, url))
    # print(auchan_product_list)
    auchan_product_dict = create_auchan_product_dict(auchan_product_list)
    print(auchan_product_dict)
    for auchan_product in auchan_product_dict.values():
        if not Food.objects.filter(categories__sold_by__grocery_name="Auchan", name=auchan_product["name"]).exists():
            new_auchan_product = Food(
                name=auchan_product['name'],
                categories=Category.objects.get(category_id=auchan_product['category']),
                product_link=auchan_product['product_url'],
                is_vegan=auchan_product['is_vegan'],
                is_cooled=auchan_product['is_cooled'],
                is_local_product=auchan_product['is_local_product'],
                is_hungarian_product=False,
                is_bio=auchan_product['is_bio'],
            )
            new_auchan_product.save()
        new_auchan_price = Price(
            food=Food.objects.filter(categories__sold_by__grocery_name="Auchan",
                                     name=auchan_product["name"]).get(),
            value=float(''.join(char for char in unicodedata.normalize('NFKD', auchan_product["price"]) if
                                char.isdigit())),
            unit=unicodedata.normalize('NFKD', auchan_product["unit_price"]).split(" ")[-1],
            unit_price=float(''.join(char for char in
                                     unicodedata.normalize('NFKD', auchan_product["unit_price"]).split("/")[0] if
                                     char.isdigit())),
        )
        new_auchan_price.save()


