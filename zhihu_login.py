#/usr/bin/python
#Filename:WeiboLogin.py
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')  


headers = {
	'Accept': '*/*',
	'Origin': 'https://www.zhihu.com',
	'X-DevTools-Emulate-Network-Conditions-Client-Id': 'A83A5B8B-3AF3-40A2-A1CE-6CD831982087',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded', 
	'charset' : 'UTF-8',
	'Referer': 'https://www.zhihu.com/',
	'Accept-Encoding': 'gzip,jj deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
}

email = "your email"
password = "your password"
remember_me = "true"

def get_xsrf(r):
	soup = BeautifulSoup(r.text)
	_xsrf = soup.find('input', attrs={'name': '_xsrf'})['value']
	return _xsrf

def login_zhihu(s, post_data):
	login_url = "https://www.zhihu.com/login/email"
	login = s.post(login_url, post_data)
	print login.text


def main():
	s = requests.session()
	r = s.get("http://www.zhihu.com/#signin", headers=headers)

	_xsrf = get_xsrf(r)

	post_data = {"email":email, "password":password, "_xsrf":_xsrf, "remember_me":remember_me}

	login_zhihu(s, post_data)



if __name__ == '__main__':
	main()