# -*- coding:utf-8 -*-
import BeautifulSoup 
import time
import urllib2

start_url = 'http://www.ruanyifeng.com/blog/2003/12/post.html'


def get_soup(url):
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup.BeautifulSoup(start_page)
	return soup


def get_next_url(url):
	soup = get_soup(url)
	next_url = soup.findAll('link', rel='next')[0].get('href')
	return next_url


def save_content(url):
	soup = get_soup(url)
	title = soup.html.title.text
	content = soup.findAll('div', id='main-content')[0]

	with open('ryf.md', 'a') as f:
		f.write(str(title))
		f.write('---')
		f.write(str(content))
		f.write('---')

	next_url = get_next_url(staurl)

	return next_url


def get_ryf(url):
	next_url = save_content(url)

	while next_url:
		next_url = save_content(next_url)


# while next_url:
# 	time.sleep(10)
# 	start_url = next_url
# 	start_page = urllib2.urlopen(start_url).read()
# 	soup = BeautifulSoup.BeautifulSoup(start_page)
# 	title = soup.html.title.text
# 	print title
# 	next_url = soup.findAll('link', rel='next')[0].get('href')
