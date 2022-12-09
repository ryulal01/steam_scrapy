import json

import scrapy

from steam.items import SteamItem


class SteamGamesSpider(scrapy.Spider):
    name = 'steam_games'
    allowed_domains = ['store.steampowered.com']

    def __init__(self, term = None, *args, **kwargs):
        super(SteamGamesSpider, self).__init__(*args, **kwargs)

        self.term = term
        self.start_urls = [
            f'https://store.steampowered.com/search/?term={term}&category1=998&ndl=1',
        ]

    def parse(self, response):
        """Парсим страницу главную"""
        response_html = response.xpath("//div[@id='search_resultsRows']")
        if response.headers[
            'Content-Type'] == b'application/json; charset=utf-8':
            results_html_from_json = json.loads(response.text).get(
                'results_html')
            response_html = scrapy.Selector(text = results_html_from_json,
                                            type = "html")

        for item in response_html.xpath("//a[contains(@href, 'app')]"):
            platforms_raw = item.xpath(
                ".//div[@class='col search_name ellipsis']/span[@class='title']/following-sibling::div/span/@class").getall()
            price = item.xpath(
                "normalize-space(.//div[contains(@class,'search_price') and contains(text(), 'pуб.')]/text())").get(
                default = '').strip()

            url_single_page = item.xpath('./@href').get()

            item = SteamItem()
            item['platforms_available'] = platforms_raw
            item['price'] = price
            item['url_single_page'] = url_single_page
            yield scrapy.Request(url_single_page,
                                 callback = self.parse_single_game,
                                 meta = {'item': item})

        if response.headers[
            'Content-Type'] == b'application/json; charset=utf-8':
            try:
                if int(response.url.split('&start=')[-1].split('&count')[
                           0]) >= 100:
                    return
            except:
                pass

        for i in range(2):
            start_value = 50 * (i + 1)
            url_next_page = f'https://store.steampowered.com/search/results/?query&start={start_value}&count=50&dynamic_data=&term={self.term}&force_infinite=1&category1=998&ndl=1&snr=1_7_7_151_7&infinite=1'
            yield scrapy.Request(url_next_page, callback = self.parse)

    def parse_single_game(self, response):
        """Парсим конкретную страницу"""
        title = response.xpath("//div[@id='appHubAppName']/text()").get(
            default = '')
        category_raw = response.xpath(
            "//div[@class='breadcrumbs']/div[@class='blockbg']/a/text()").getall()
        rating = response.xpath(
            "//div[text()='Все обзоры:']/following-sibling::div[@class='summary column']/span[contains(@class,'responsive_reviewdesc')]/text()").get(
            default = '').strip()
        release_date = response.xpath(
            "//div[@class='release_date']/div[text()='Дата выхода:']/following-sibling::div[@class='date']/text()").get(default = '')
        game_developers_raw = response.xpath(
            "//div[@class='dev_row']/div[text()='Разработчик:']/following-sibling::div[@id='developers_list']/a/text()").getall()
        tags_raw = response.xpath(
            "//div[text()='Популярные метки для этого продукта:']/following-sibling::div//a/text()").getall()

        item = response.meta['item']
        item['title'] = title
        item['category'] = category_raw
        item['rating'] = rating
        item['release_date'] = release_date
        item['game_developers'] = game_developers_raw
        item['tags'] = tags_raw

        yield item