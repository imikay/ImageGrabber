from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.http.request import Request
from scrapy.item import Item
from ImageGrabber.items import ImageItem


class ImageSpider(CrawlSpider):
    name = '7te.org'
    #allowed_domains = ['http://www.7te.org']
    start_urls = ['http://www.7te.org/browse/1024x768/page-1.html']
    rules = (
        Rule(SgmlLinkExtractor(allow=(".",)), callback='parse_item', follow=True),        
    )
    
    def parse_item(self, response):                                            
        loader = XPathItemLoader(item = ImageItem(), response = response)
        loader.add_xpath('image_urls', '//img/@src')   
        
        return loader.load_item()