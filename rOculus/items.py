# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RoculusItem(scrapy.Item):
	title = scrapy.Field()
	upvotes = scrapy.Field()
	comments = scrapy.Field()
	link = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
	pass
