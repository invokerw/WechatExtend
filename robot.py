#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf8")

KEY = '2b76b9f122b44d978a11c459e4b1e4dd'  #聊天开启
KEY1 = '7e31086f308e400c937b644c5a974a2e'  #聊天关闭
#'8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg,key):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : key,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()

        if r.get('code') == 200000:
            return r.get('text').encode('utf-8') + "戳-->"+ r.get('url').encode('utf-8')
        else : 
            return r.get('text').encode('utf-8')
    except:
        return "机器人抛了个异常..."
def get_response_nochat(msg):
	return get_response(msg, KEY1)
def get_response_chat(msg):
	return get_response(msg, KEY)

def main():
	reply = get_response_nochat("图片")
	#reply = get_response_nochat("你是")
	print('say:' + reply)


if __name__ == '__main__':
	main()
