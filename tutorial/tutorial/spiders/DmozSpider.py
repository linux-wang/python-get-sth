#Filename:DmozSpider.py
#-*- coding:utf-8 -*-

import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
	"""use for tutorial"""
	name = "dmoz"
	allow_urls = ["dmoz.org"]
	start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	]

	def parse(self, response):
		for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_articles_follow_next_page)

	def parse_articles_follow_next_page(self, response):
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath("a/@href").extract()
			item['desc'] = sel.xpath("text()").extract()

			yield item

		next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
		if next_page:
			url = response.urljoin(next_page[0].extract())
	        yield scrapy.Request(url, self.parse_articles_follow_next_page)

