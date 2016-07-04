# -*- coding:utf-8-*-
import BeautifulSoup 
import time
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')


start_url = 'http://www.ruanyifeng.com/blog/2011/03/china_celebrity_gossips_pre-1949.html'


def get_soup(url):
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup.BeautifulSoup(page)
	return soup


def get_next_url(soup):
	next_url = soup.findAll('link', rel='next')[0].get('href')
	return next_url


def save_content(url):
	soup = get_soup(url)
	title = soup.html.title.text
	content = soup.findAll('div', id='main-content')[0]

	with open('ryf.md', 'a') as f:
		f.write(title)
		f.write('---')
		f.write(str(content))
		f.write('---')

	next_url = get_next_url(soup)

	return next_url


def get_ryf(url):
	next_url = save_content(url)

	time.sleep(5)

	while next_url:
		_url = save_content(next_url)
		if _url:
			print _url
			next_url = _url
		else:
			print 'finished'
	
if __name__ == '__main__':
	get_ryf(start_url)


# while next_url:
# 	time.sleep(5)
# 	start_url = next_url
# 	start_page = urllib2.urlopen(start_url).read()
# 	soup = BeautifulSoup.BeautifulSoup(start_page)
# 	title = soup.html.title.text
# 	print title
# 	next_url = soup.findAll('link', rel='next')[0].get('href')
