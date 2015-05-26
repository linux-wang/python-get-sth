#Filename:pm25.py

import urllib2
from bs4 import BeautifulSoup

def getUrl(city_name):
    url1="http://www.pm25.com/"
    url2=".html"
    url=url1+city_name+url2
    return url

def getHtml(url):
    page=urllib2.urlopen(url).read()
    return page

def getPM25(city_name,page):
    html=BeautifulSoup(page)
    CityName=city_name
    Aqi=html.find("a",{"class","bi_aqiarea_num"}).text
    print"======================"
    print "This is the result:"
    print CityName
    print "AQI:",Aqi
     
def main():    
    print"======================"
    print "input a cityname:"
    city_name=raw_input()
    url=getUrl(city_name)
    page=getHtml(url)
    getPM25(city_name,page)
    print"======================"

if __name__=="__main__":
    main()
