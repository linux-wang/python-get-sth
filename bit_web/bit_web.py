# -*- coding:utf-8 -*-
 
import socket

import requests

from account_conf import *

def is_online():
    ip = socket.gethostbyname(socket.gethostname())
    check_result = requests.post(auth_url, data={'ip': ip, 'action': 'get_online_info'})
    if check_result.content == 'not_online':
        return False
    return True


def login():
    login_res = requests.post(auth_url, data=login_data)
    if login_res.content.startswith('login_ok'):
        print u"登录成功"
        return 
    print login_res.content


def logout():
    logout_res = requests.post(auth_url, data=logout_data)
    print logout_res.content


if __name__ == '__main__':
    if is_online():
        logout()
    else:
        login()
