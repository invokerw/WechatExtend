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
		reply = reply + "...|..." +getweather.get_weather(101020100)
		print('I say:'+reply)
		return reply
	elif msg['Text'].encode('utf-8') == "关闭回复":
		reply = '好的,我闭嘴'
		chat = 0
		return reply
	elif msg['Text'].encode('utf-8') == "提问模式":
		reply = '切换至提问模式'
		chat = 1
		return reply
	elif msg['Text'].encode('utf-8') == "开启聊天":
		reply = '切换至聊天模式'
		chat = 2
		return reply
	else:
		if chat == 0:
			return
		elif chat == 1:
			reply = robot.get_response_nochat(msg['Text'])
		elif chat == 2:
			reply = robot.get_response_chat(msg['Text'])
		if reply == msg['Text']:
			return
		print('robot say:'+reply)
		return reply
	#return reply or defaultReply

def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
