BOT_NAME = 'steam'

SPIDER_MODULES = ['steam.spiders']
NEWSPIDER_MODULE = 'steam.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 3

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}



ITEM_PIPELINES = {
   'steam.pipelines.DatePipeline': 300,
   'steam.pipelines.PlatformsPipeline': 301,
   'steam.pipelines.CategoryPipeline': 301,
   'steam.pipelines.TagsPipeline': 302,
   'steam.pipelines.GameDevPipeline': 303,
}


REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'


FEED_EXPORT_ENCODING = 'utf-8'