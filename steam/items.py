import scrapy


class SteamItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    platforms_available = scrapy.Field()
    url_single_page = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    release_date = scrapy.Field()
    game_developers = scrapy.Field()
    tags = scrapy.Field()
