import logging
import re
import time
import unicodedata
import requests
from decimal import Decimal
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
# from PIL import Image
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


def check_availability_of_auchan_item(product_div) -> str:
    item_availability = "Nincs készleten"
    if product_div.find("div", class_='_2djl'):
        item_availability = product_div.find("div", class_='_2djl').text
    return item_availability


def save_image_of_spar_product(product_div, model_instance, **kwargs):
    image = product_div.find('img')
    image_url = image['src']

    # img = Image.open(requests.get(image_url, stream=True).raw)

    # img.save(f'{kwargs.get("product_name", "image")}.jpg')
    r = requests.get(image_url)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()

    model_instance.photo.save(f'{kwargs.get("product_name", "image")}.jpg', File(img_temp), save=True)


def save_image_of_auchan_product(product_div, model_instance, **kwargs):
    image = product_div.find("picture", class_='_lrgv')
    #  image_url = image['srcset']
    image_url = image.find('source', {'type': 'image/webp'})["srcset"]

    # img = Image.open(requests.get(image_url, stream=True).raw)

    # img.save(f'{kwargs.get("product_name", "image")}.jpg')
    r = requests.get(image_url)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()

    model_instance.photo.save(f'{kwargs.get("product_name", "image")}.jpg', File(img_temp), save=True)


# def save_image_from_url(model, url):
#     r = requests.get(url)
#
#     img_temp = NamedTemporaryFile(delete=True)
#     img_temp.write(r.content)
#     img_temp.flush()
#
#     model.image.save("image.jpg", File(img_temp), save=True)


def scrape_auchan_hrefs(driver) -> list:
    """Scrape Auchan categories and put them into a list"""
    # driver = launch_broswer('https://online.auchan.hu/shop')
    driver.get('https://online.auchan.hu/shop')
    time.sleep(0.5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(0.3)
    #  driver.find_element(By.CLASS_NAME, '_1DRX').click()
    #  time.sleep(0.3)
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
    # total_height = int(driver.execute_script("return document.body.scrollHeight"))
    total_height = 2001

    while y <= total_height:
        elements = driver.find_elements(By.CLASS_NAME, '_48TB')
        for WebElement in elements:
            element_html = WebElement.get_attribute('outerHTML')  # gives exact HTML content of the element
            element_soup = BeautifulSoup(element_html, 'html.parser')
            product_list.append(element_soup)
        y += 500
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        # total_height = int(driver.execute_script("return document.body.scrollHeight"))
        time.sleep(1.5)

    return product_list


def create_or_update_auchan_products(html_product_list) -> None:
    for productDiv in html_product_list:
        badge_names = [image['alt'] for image in productDiv.find_all("img", class_='_2Py5')]
        product_name = productDiv.find("a", class_='_2J-k').find("span").text
        is_cooled = False
        is_local_product = False
        is_bio = False
        if badge_names:
            for badge_name in badge_names:
                if badge_name.strip() == "Hűtött termék":
                    is_cooled = True
                if badge_name.strip() == "Magyar termék":
                    is_local_product = True
                if "Hazai Termék" in badge_name.strip():
                    is_local_product = True
                if badge_name.strip() == "BIO":
                    is_bio = True
        if not Item.objects.filter(categories__sold_by__grocery_name="Auchan", name=product_name).exists():
            new_auchan_item = Item(
                name=product_name,
                categories=Category.objects.filter(sold_by__grocery_name="Auchan").get(),
                is_vegan=False,
                is_cooled=is_cooled,
                is_local_product=is_local_product,
                is_bio=is_bio,
                on_stock=check_availability_of_auchan_item(productDiv),
                product_link=dict.fromkeys(filter(('javascript: void(0)').__ne__, [category['href'] for category in
                                                                                  productDiv.find_all(
                                                                                      "a", href=True)])).keys()
            )
            save_image_of_auchan_product(productDiv, new_auchan_item, product_name=product_name)
            new_auchan_item.save()


def create_or_update_auchan_prices(html_product_list) -> None:
    for productDiv in html_product_list:
        badge_names = [image['alt'] for image in productDiv.find_all("img", class_='_2Py5')]
        product_name = productDiv.find("a", class_='_2J-k').find("span").text
        product_price = productDiv.find("div", class_='_3vje').text
        sale_price = product_price
        unit_price = productDiv.find("div", class_='_20Mg').text
        if badge_names:
            for badge_name in badge_names:
                if badge_name.strip() == "Kiemelt termék":
                    sale_price = productDiv.find("div", class_='X9nF').text
        new_auchan_price = Price(
            item=Item.objects.filter(categories__sold_by__grocery_name="Auchan",
                                     name=product_name).get(),
            value=Decimal(''.join(char for char in unicodedata.normalize('NFKD', product_price) if
                                char.isdigit())),
            sale_value=Decimal(''.join(char for char in unicodedata.normalize('NFKD', sale_price) if
                                     char.isdigit())),
            unit=unicodedata.normalize('NFKD', unit_price).split(" ")[-1],
            unit_price=Decimal(''.join(char for char in
                                     unicodedata.normalize('NFKD', unit_price).split("/")[0] if
                                     char.isdigit())),
        )
        new_auchan_price.save()


def update_auchan_product_table():
    driver = launch_broswer('https://online.auchan.hu/shop')
    auchan_href_list = scrape_auchan_hrefs(driver)
    auchan_category_url_list = extract_auchan_categories(auchan_href_list)
    combined_auchan_product_list = []
    for url in auchan_category_url_list[:1]:
        combined_auchan_product_list.extend(scrape_auchan_products(driver, url))
    # print(auchan_product_list)
    create_or_update_auchan_products(combined_auchan_product_list)
    create_or_update_auchan_prices(combined_auchan_product_list)


def scrape_spar_categories() -> list:
    spar_main_page = requests.get("https://www.spar.hu/onlineshop/")
    spar_main_page_soup = BeautifulSoup(spar_main_page.content, 'html.parser')
    category_set = spar_main_page_soup.find_all("a", class_="flyout-categories__link")
    spar_href_list = list(filter(('javascript:void(0)').__ne__, [category['href'] for category in category_set]))

    # print(spar_href_list)
    return spar_href_list


def scrape_spar_product_html_list(driver, category_url) -> list:
    """Scrape SPAR product info for a given category"""
    driver.get(f"https://www.spar.hu{category_url}")

    html_product_list = []
    y = 500
    total_height = 2001

    while y <= total_height:
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        elements = driver.find_elements(By.CLASS_NAME, 'productBox')
        for WebElement in elements:
            element_html = WebElement.get_attribute('outerHTML')  # gives exact HTML content of the element
            element_soup = BeautifulSoup(element_html, 'html.parser')
            html_product_list.append(element_soup)
        time.sleep(1.5)

    return html_product_list


def create_or_update_spar_products(html_product_list) -> dict:
    for productBox in html_product_list:
        badge_name = productBox.find("div", class_='badgeName')
        product_name = productBox.find("a", id=lambda x: x and x.startswith('product-')).text
        is_cooled = False
        is_local_product = False
        is_bio = False
        if badge_name:
            if badge_name.text.strip() == "Hűtött":
                is_cooled = True
            if badge_name.text.strip() == "Hazai Termék":
                is_local_product = True
            if badge_name.text.strip() == "BIO":
                is_bio = True
        if not Item.objects.filter(categories__sold_by__grocery_name="SPAR", name=product_name).exists():
            new_spar_item = Item(
                name=product_name,
                categories=Category.objects.filter(sold_by__grocery_name="SPAR").get(),
                is_vegan=False,
                is_cooled=is_cooled,
                is_local_product=is_local_product,
                is_bio=is_bio,
                on_stock='Készleten',
                product_link=[category['href'] for category in productBox.find_all("a", href=True)][0]
            )

            save_image_of_spar_product(productBox, new_spar_item, product_name=product_name)
            new_spar_item.save()


def create_or_update_spar_prices(html_product_list) -> None:
    for productDiv in html_product_list:
        badge_name = productDiv.find("div", class_='badgeName')
        product_name = productDiv.find("a", id=lambda x: x and x.startswith('product-')).text
        product_price = productDiv.find("label", class_='priceInteger').text
        sale_price = product_price
        unit_price = productDiv.find("label", class_='extraInfoPrice').text
        if badge_name:
            if badge_name.text.strip() == "Akció":
                sale_price = productDiv.find("label", class_='insteadOfPrice').text,
        new_spar_price = Price(
            item=Item.objects.filter(categories__sold_by__grocery_name="Auchan",
                                     name=product_name).get(),
            value=Decimal(''.join(char for char in
                                     unicodedata.normalize('NFKD', product_price) if
                                     char.isdigit())),
            sale_value=Decimal(''.join(char for char in
                                     unicodedata.normalize('NFKD', sale_price) if
                                     char.isdigit())),
            unit=unit_price.split("/")[-1],
            unit_price=Decimal(''.join(char for char in
                                     unicodedata.normalize('NFKD', unit_price).split(",")[0] if
                                     char.isdigit())),
        )
        new_spar_price.save()


def update_spar_product_table():
    spar_category_url_list = scrape_spar_categories()
    driver = launch_broswer('https://www.spar.hu/onlineshop/')
    spar_product_list = []
    for url in spar_category_url_list[:1]:
        spar_product_list.extend(scrape_spar_product_html_list(driver, url))
    # print(auchan_product_list)
    create_or_update_spar_products(spar_product_list)
    create_or_update_spar_prices(spar_product_list)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # update_spar_product_table()
        update_auchan_product_table()

