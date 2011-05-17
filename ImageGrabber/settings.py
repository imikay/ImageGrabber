# Scrapy settings for ImageGrabber project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME    = 'ImageGrabber'
BOT_VERSION = '1.0'

# Random interval between 0.5 and 1.5 * DOWNLOAD_DELAY
DOWNLOAD_DELAY     = 5 
SPIDER_MODULES     = ['ImageGrabber.spiders']
NEWSPIDER_MODULE   = 'ImageGrabber.spiders'
DEFAULT_ITEM_CLASS = 'ImageGrabber.items.ImageItem'

# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT     = "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0"
IM_MODULE      = 'ImageGrabber.pipelines.MyImagePipeline'
ITEM_PIPELINES = ['ImageGrabber.pipelines.MyImagePipeline']

# Where we store the images, in this case they will be stored 
# in E:/ImageGrabber/full directory.
IMAGES_STORE = 'E:/ImageGrabber'

# Specify the min height and width of the image to download
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH  = 110




