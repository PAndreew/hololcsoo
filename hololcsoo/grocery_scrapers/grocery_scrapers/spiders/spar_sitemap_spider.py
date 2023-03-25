import scrapy
#from hololcsoo.hololcsoo.utils import


class SparSitemapSpider(scrapy.spiders.SitemapSpider):
    name = "spar_sitemap_spider"
    #sitemap_urls = ['https://www.spar.hu/onlineshop/medias/sys_master/root/h4d/ha6/10144644431902/Product-hu-HUF-7763662366745958785.xml']
    sitemap_urls = ['https://online.auchan.hu/sitemap-products.xml']
    #sitemap_rules = [('/onlineshop/', 'parse_product')]

    def parse(self, response):
        yield {
            'url': response.url,
        }

    def closed(self, reason):
        urls = set()
        for item in self.crawler.stats.get_stats():
            if item.startswith('item_scraped_count'):
                urls = urls.union(set(self.crawler.stats.get_value(item)))
        return urls