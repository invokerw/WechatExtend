#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import itchat
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

@itchat.msg_register(itchat.content.TEXT)#,isGroupChat=True)
def tuling_reply(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	defaultReply = u'I received:'+msg['Text'].encode('utf-8')
	reply = get_response(msg['Text'])
	print('I say:'+reply)
	return reply or defaultReply

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_chatroom(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	defaultReply = u'I received:'+msg['Text'].encode('utf-8')
	reply = get_response(msg['Text'])
	print('I say:'+reply)
	return reply or defaultReply
def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
