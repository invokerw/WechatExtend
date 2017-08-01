#!/usr/bin/python
# -*- coding:utf-8 -*-
import itchat
import sys
import robot
import getweather

reload(sys)
sys.setdefaultencoding("utf8")

chat = 0

#群聊消息接收 isGroupChat=True
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_chatroom(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	reply = ""
	global chat
	defaultReply = 'I received:'+msg['Text'].encode('utf-8')
	if msg['Text'].encode('utf-8') == "天气":
		reply = getweather.get_weather(101010100)
		reply = reply + "......." +getweather.get_weather(101020100)
		print('I say:'+reply)
		return reply
	elif msg['Text'].encode('utf-8') == "关闭聊天":
		reply = '关闭聊天成功'
		chat = 0
		return reply
	elif msg['Text'].encode('utf-8') == "开启聊天":
		reply = '开启聊天成功'
		chat = 1
		return reply
	else:
		if chat == 0:
			return
		reply = robot.get_response(msg['Text'])
		print('robot say:'+reply)
		return reply
	#return reply or defaultReply

def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
