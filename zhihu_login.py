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

email1 = "your email"
password1 = "your password"
remember_me1 = "true"

class zhihu_login():
	"""use for signin zhihu"""
	def __init__(self, email, password, remember_me):
		self.email = email
		self.password = password
		self.remember_me = remember_me

	def get_session(self):
		s = requests.session()
		return s

	def get_request(self):
		s = self.get_session()
		r = s.get("http://www.zhihu.com/#signin", headers=headers)
		return r

	def get_post_data(self):
		_xsrf = self.get_xsrf()
		post_data = {"email":self.email, "password":self.password, "_xsrf":_xsrf, "remember_me":self.remember_me}
		return post_data

	def get_xsrf(self):
		r = self.get_request()
		soup = BeautifulSoup(r.text)
		_xsrf = soup.find('input', attrs={'name': '_xsrf'})['value']
		return _xsrf

	def login_zhihu(self):
		s = self.get_session()
		post_data = self.get_post_data()
		login_url = "https://www.zhihu.com/login/email"
		login = s.post(login_url, post_data)
		print login.text


def main():
#	s = requests.session()
#	r = s.get("http://www.zhihu.com/#signin", headers=headers)

#	_xsrf = get_xsrf(r)

#	post_data = {"email":email, "password":password, "_xsrf":_xsrf, "remember_me":remember_me}
	signin = zhihu_login(email1, password1, remember_me1)
	signin.login_zhihu()

if __name__ == '__main__':
	main()
