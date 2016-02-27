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

next_page_link = []

def download_pic(url):
		first_name = url[-18:]
		path = "D:\\py\\pictures\\"+first_name
		name = path.replace('/','_')
		if not os.path.exists(name):
			data = urllib.urlretrieve(url, name)
		else:
			print "this pic already exists, no more download"
			pass

class meizitu_spider(scrapy.Spider):
	"""get the pictures of meizitu.com"""
	
	name = "meizitu_spider"		
	start_urls = ["http://www.meizitu.com/a/list_1_1.html"]
	allow_urls = ["meizitu.com"]

	def parse(self, response):
		for href in response.xpath("//ul[@class='wp-list clearfix']/li/div/div/a/@href").extract():
			yield scrapy.Request(href, callback=self.parse_picture)

		#how to get the next page url
		pages_link = response.xpath("//div[@id='wp_page_numbers']/ul/li/a/@href").extract()
		full_page_link = "http://www.meizitu.com/a/"+pages_link[-2]
		if full_page_link not in next_page_link:
			next_page_link.append(full_page_link)
			yield scrapy.Request(full_page_link, callback=self.parse)
		else:
			print '''
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************

			I finished everthing but I can't exit by myself, so please enter 'ctrl+c' to quit, thank you

			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			*********************************************************************************************
			'''

	def parse_picture(self, response):
		item = MeizituSpiderItem()
		item['pic_name'] = response.selector.xpath("//title/text()").extract(),
		item['pic_url'] = response.selector.xpath("//div/p/img/@src").extract()
		yield item		
		#for url in item['pic_url']:
		#	download_pic(url)

		




