from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class DatePipeline:
	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		release_date = adapter.get('release_date')
		if release_date == 'Скоро выйдет':
			return item
		if release_date:
			release_date_year = release_date.split(' ')[-1]
			if release_date_year.isdigit():
				if int(release_date_year) <= 2000:
					raise DropItem(f"Год меньше 2000 {item}")
		return item


class PlatformsPipeline:
	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		platforms = adapter.get('platforms_available')
		platforms_string = ', '.join(
			[platform.split('platform_img')[-1].strip() for platform in
			 platforms])
		adapter['platforms_available'] = platforms_string
		return item


class CategoryPipeline:
	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		category_raw = adapter.get('category')
		title = adapter.get('title')

		if title in category_raw:
			category_raw.remove(title)

		if len(category_raw) > 1:
			category_raw = category_raw[1:]

		if len(category_raw) >= 1:
			category = ' | '.join(
				[category.strip() for category in category_raw])
		else:
			category = 'Нет категории'
		adapter['category'] = category
		return item


class TagsPipeline:
	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		tags_raw = adapter.get('tags')
		tags = ', '.join([tag.strip() for tag in tags_raw])
		adapter['tags'] = tags
		return item


class GameDevPipeline:
	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		game_developers_raw = adapter.get('game_developers')
		game_developers = ', '.join(game_developers_raw)
		adapter['game_developers'] = game_developers
		return item

