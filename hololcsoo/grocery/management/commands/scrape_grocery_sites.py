import logging
import requests
import xml.etree.ElementTree as ET
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from grocery_scrapers.grocery_scrapers.spiders.spar_sitemap_spider import SparSitemapSpider
from django.core.management.base import BaseCommand
#import hololcsoo.utils as utils
# from PIL import Image

logger = logging.getLogger(__name__)

def get_sitemap_urls(sitemap_url):
    # Fetch the sitemap.xml page
    response = requests.get(sitemap_url)

    # Parse the XML content of the sitemap.xml page
    root = ET.fromstring(response.content)

    # Find all the 'loc' elements in the XML content
    locs = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')

    # Extract the text content of the 'loc' elements and store them in a set
    urls = set()
    for loc in locs:
        urls.add(loc.text)

    # Return the URLs as a set
    return urls

class Command(BaseCommand):
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(SparSitemapSpider)
        process.start()
        # update_spar_product_table()
        #update_auchan_product_table()

