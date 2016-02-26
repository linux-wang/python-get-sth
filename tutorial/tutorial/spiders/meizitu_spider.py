#Filename:meizitu_spider.py
#-*- encoding:utf-8 -*-

import scrapy
from tutorial.items import MeizituSpiderItem
import urllib
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

def download_pic(url):
		first_name = url[-18:]
		path = "D:\\py\\pictures\\"+first_name
		name = path.replace('/','_')
		if not os.path.exists(name):
			data = urllib.urlretrieve(url, name)
		else:
			print "**************************pass****************************"
			pass

class meizitu_spider(scrapy.Spider):
	"""get the pictures of meizitu.com"""
	
	name = "meizitu_spider"		
	start_urls = ["http://www.meizitu.com/"]
	allow_urls = ["meizitu.com"]

	def parse(self, response):
		for href in response.selector.xpath("//h2/a/@href").extract():
			print href              #add for test
			yield scrapy.Request(href, callback=self.parse_next_page_picture)

	def parse_next_page_picture(self, response):
		item = MeizituSpiderItem()
		item['pic_name'] = response.selector.xpath("//title/text()").extract(),
		item['pic_url'] = response.selector.xpath("//div/p/img/@src").extract()
		yield item		
		for url in item['pic_url']:
			download_pic(url)

		#how to get the next page url
		#next_page = "www.meizitu.com"+response.selector.xpath("//li").extract()







