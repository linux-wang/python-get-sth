#Filename:getOne.py

import sys,urllib,urllib2
from bs4 import BeautifulSoup
import re

reload(sys)
sys.setdefaultencoding("utf-8")

def getHtml(url):
#	req_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#	'Accept':'text/html;q=0.9,*/*;q=0.8',
#	'Accept-Charset':'utf-8;q=0.7,*;q=0.3',
#	'Accept-Encoding':'gzip',
#	'Connection':'close',
#	'Referer':None}
	
	page=urllib.urlopen(url)
	return page.read()

def getPassage(html):
#get the head
	passage=BeautifulSoup(html)
	head=passage.h2.string
	head.strip(str(head))
#	print head

#get the author	
	author_1=passage.find_all('p','articulo-autor')
	re_h=re.compile('<[^>]*>]{1}')
	author_2=re_h.sub('',str(author_1))
	re_h_test=re.compile('<[^>]*>')
	author_3=re_h_test.sub('',str(author_2))
	re_h_test_1=re.compile('[\\[]')
	author=re_h_test_1.sub('',author_3)
#	print author

	
	para = re.compile(u'<div class="articulo-contenido">.*?</div>', re.DOTALL)
	style=para.search(html.decode("utf-8"))
	if style:
		html=style.group(0)
	#	print "found it "
	else:
		print "not found"
	
	para = re.sub('<[^>]*>', '', html)
	content=para.encode("utf-8")
#	print content
	OnePassage=head+author+content
#	print One
	return OnePassage


url_1="http://www.wufazhuce.com/one/vol."
url_3="#articulo"
for i in range(911,912):
	url_2=str(i)
	url=url_1+url_2+url_3	
		
	page_one=getHtml(url)
	OnePassage=getPassage(page_one)
	filename=url_2+".txt"
	f=file(filename,'w')
	f.write(OnePassage)
	f.close
	
