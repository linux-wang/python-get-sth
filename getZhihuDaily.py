#Filename:getZhihu.py
import re,os
import urllib2
from bs4 import BeautifulSoup
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")



def getHtml(url):
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1','Referer' : '******'}
    request=urllib2.Request(url,None,header)
    response=urllib2.urlopen(request)
    text=response.read()
    return text

def mkDir():
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    os.mkdir(str(date))
    
def saveText(text):
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    dir_name="/home/wang/Documents/py/Zhihu/"+date
    soup=BeautifulSoup(text)
#    i=1
#    for i in soup.h2:
#        i=i+1
    if soup.h2.get_text()=='':
        filename=dir_name+"/ad.txt"
        fp=file(filename,'w')
        content=soup.find('div',"content")
        content=content.get_text()
        fp.write(content)
        fp.close()

#    elif i > 1:
#        filename=dir_name+"/kiding.txt"
#        contents=soup.findAll('div',"content")+soup.findAll("div","question")
#        contents=contents.get_text()
#        fp=file(filename,'w')
#        fp.write(contents)
#        fp.close()

    else:
        filename=dir_name+"/"+soup.h2.get_text()+".txt"
        fp=file(filename,'w')
        content=soup.find('div',"content")
        content=content.get_text()
        fp.write(content)
        fp.close()
    
#   print content #test

def getUrl(url):
    html=getHtml(url) 
    
#   print html
    soup=BeautifulSoup(html)
    urls_page=soup.find('div',"post-body")
#   print urls_page

    urls=re.findall('"((http)://.*?)"',str(urls_page))
    return urls 

def main():
    mkDir()
    page="http://zhihudaily.ahorn.me"
    urls=getUrl(page)
    for url in urls:
        text=getHtml(url[0])
        saveText(text)

if __name__=="__main__":
    main()

#url="http://daily.zhihu.com/story/4671450"
#url="http://zhihudaily.ahorn.me"
#text=getHtml(url)
#saveText(text)
#getUrl(url)
