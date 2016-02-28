#!/usr/lib/bin
#Filename:youdao.py

#coding="utf-8"

import urllib2
import sys
import json


def translate(url, word):
	html = urllib2.urlopen(url+word)
#	print "result:"+html.read()
	result = html.read()
	js = json.loads(result)
	for item in js:
		if item=="translation":
			translation = js[item]
		else:
			pass
	print "translation:", translation

def main():
	url = "http://fanyi.youdao.com/openapi.do?keyfrom=oldfriends-wang&key=1908356382&type=data&doctype=json&version=1.1&q="
	word = raw_input("word:")
	translate(url, word)


if __name__=="__main__":
	main()


