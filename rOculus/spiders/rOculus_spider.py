import scrapy
from scrapy.item import Item, Field
from rOculus.items import RoculusItem

class rOculusSpider(scrapy.Spider):
	name = "rOculus"
	allowed_domains = ["reddit.com"]
	start_urls = ["http://reddit.com/r/oculus/top/?sort=top&t=week"]

	def parse(self, response):
		#sel = Selector(response)
		#sites=sel.css('.thing')
		for sel in response.css('.thing'):	
			item = RoculusItem()
			item['upvotes'] = sel.css('div.score.unvoted ::text').extract()
			item['title'] = sel.css('a.title.may-blank ::text').extract()
			item['link'] = sel.css('a.title[href]::attr(href)').extract()
			print item['upvotes']
			print item['title']
			print item['link']
