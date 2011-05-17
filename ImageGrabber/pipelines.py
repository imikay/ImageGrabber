# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline, ImageException
from scrapy.http import Request
from cStringIO import StringIO
import psycopg2
import hashlib
from scrapy.conf import settings

class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x) for x in item.get('image_urls', [])]   
        
    def item_completed(self, results, item, info):
        item['images'] = [x for ok, x in results if ok]
        return item
    
    # Override the convert_image method to disable image conversion    
    def convert_image(self, image, size=None):
        buf = StringIO()        
        try:
            image.save(buf, image.format)
        except Exception, ex:
            raise ImageException("Cannot process image. Error: %s" % ex)

        return image, buf    
        
    def image_key(self, url):
        image_guid = hashlib.sha1(url).hexdigest()
        return 'full/%s.jpg' % (image_guid)    
