import logging
import re
import time
import unicodedata
import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from grocery.models import Item, Price, Category

logger = logging.getLogger(__name__)

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


def save_image_of_product(product_div, **kwargs):
    image = product_div.find('img')
    image_url = image['src']

    img = Image.open(requests.get(image_url, stream=True).raw)

    img.save(f'{kwargs.get("product_name", "image")}.image.jpg')


def scrape_auchan_hrefs(driver) -> list:
    """Scrape Auchan categories and put them into a list"""
    # driver = launch_broswer('https://online.auchan.hu/shop')
    driver.get('https://online.auchan.hu/shop')
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
        total_height = int(driver.execute_script("return document.body.scrollHeight"))
        time.sleep(1.5)

    return product_list


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
            'sale_price': productDiv.find("div", class_='_3vje').text,
            'unit_price': productDiv.find("div", class_='_20Mg').text,
            'is_vegan': False,
            'is_cooled': False,
            'is_local_product': False,
            'is_bio': False,
            'on_stock': True,
            'on_sale': False,
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
                if badge_name.strip() == "Kiemelt termék":
                    product_dict[product_name]['on_sale'] = True
                    product_dict[product_name]['sale_price'] = productDiv.find("div", class_='X9nF').text

    return product_dict


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
        if not Item.objects.filter(categories__sold_by__grocery_name="Auchan", name=auchan_product["name"]).exists():
            new_auchan_product = Item(
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
            food=Item.objects.filter(categories__sold_by__grocery_name="Auchan",
                                     name=auchan_product["name"]).get(),
            value=float(''.join(char for char in unicodedata.normalize('NFKD', auchan_product["price"]) if
                                char.isdigit())),
            unit=unicodedata.normalize('NFKD', auchan_product["unit_price"]).split(" ")[-1],
            unit_price=float(''.join(char for char in
                                     unicodedata.normalize('NFKD', auchan_product["unit_price"]).split("/")[0] if
                                     char.isdigit())),
        )
        new_auchan_price.save()


def scrape_spar_categories() -> list:
    spar_main_page = requests.get("https://www.spar.hu/onlineshop/")
    spar_main_page_soup = BeautifulSoup(spar_main_page.content, 'html.parser')
    category_set = spar_main_page_soup.find_all("a", class_="flyout-categories__link")
    spar_href_list = list(filter(('javascript:void(0)').__ne__, [category['href'] for category in category_set]))

    # print(spar_href_list)
    return spar_href_list


def scrape_spar_products(driver, category_url) -> list:
    """Scrape SPAR product info for a given category"""
    driver.get(f"https://www.spar.hu{category_url}")

    product_list = []
    y = 500
    total_height = 2001

    while y <= total_height:
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        elements = driver.find_elements(By.CLASS_NAME, 'productBox')
        for WebElement in elements:
            element_html = WebElement.get_attribute('outerHTML')  # gives exact HTML content of the element
            element_soup = BeautifulSoup(element_html, 'html.parser')
            product_list.append(element_soup)
        time.sleep(1.5)

    return product_list


def create_spar_product_dict(html_product_list) -> dict:
    product_dict = {}

    for productBox in html_product_list:
        badge_name = productBox.find("div", class_='badgeName')
        product_name = productBox.find("a", id=lambda x: x and x.startswith('product-')).text
        save_image_of_product(productBox, product_name=product_name)
        product_dict[product_name] = {
            'name': product_name,
            'sold_by': 'SPAR',
            'price': productBox.find("label", class_='priceInteger').text,
            'sale_price': productBox.find("label", class_='priceInteger').text,
            'unit_price': productBox.find("label", class_='extraInfoPrice').text,
            'is_vegan': False,
            'is_cooled': False,
            'is_local_product': False,
            'is_bio': False,
            'on_stock': 'Készleten',
            'product_url': [category['href'] for category in productBox.find_all("a", href=True)][0]
        }
        if badge_name:
            if badge_name.text.strip() == "Hűtött":
                product_dict[product_name]['is_cooled'] = True
            if badge_name.text.strip() == "Hazai Termék":
                product_dict[product_name]['is_local_product'] = True
            if badge_name.text.strip() == "BIO":
                product_dict[product_name]['is_bio'] = True
            if badge_name.text.strip() == "Akció":
                product_dict[product_name]['sale_price'] = productBox.find("label", class_='insteadOfPrice').text,

    return product_dict


def update_spar_product_table():
    spar_category_url_list = scrape_spar_categories()
    driver = launch_broswer('https://www.spar.hu/onlineshop/')
    spar_product_list = []
    for url in spar_category_url_list[:2]:
        spar_product_list.extend(scrape_spar_products(driver, url))
    # print(auchan_product_list)
    spar_product_dict = create_spar_product_dict(spar_product_list)
    print(spar_product_dict)


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_auchan_product_table()

