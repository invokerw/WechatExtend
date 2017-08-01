#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf8")

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text').encode('utf-8')
    except:
        return

def main():
	reply = get_response("113")
	print('say:' + reply)


if __name__ == '__main__':
	main()