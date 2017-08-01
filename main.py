#!/usr/bin/python
# -*- coding:utf-8 -*-
import itchat
import sys
import robot
import getweather

reload(sys)
sys.setdefaultencoding("utf8")


#群聊消息接收 isGroupChat=True
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_chatroom(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	reply = ""
	defaultReply = 'I received:'+msg['Text'].encode('utf-8')
	if msg['Text'].encode('utf-8') == "天气":
		reply = getweather.get_weather(101010100)
		reply = reply + "......." +getweather.get_weather(101020100)
		print('I say:'+reply)
		return reply
	else:
		reply = robot.get_response(msg['Text'])
	#return reply or defaultReply

def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
