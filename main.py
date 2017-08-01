#!/usr/bin/python
# -*- coding:utf-8 -*-
import itchat
import sys
import robot

reload(sys)
sys.setdefaultencoding("utf8")


#非群聊消息接收
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	defaultReply = u'I received:'+msg['Text'].encode('utf-8')
	reply = robot.get_response(msg['Text'])
	print('I say:'+reply)
	return reply or defaultReply

#群聊消息接收
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_chatroom(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	defaultReply = u'I received:'+msg['Text'].encode('utf-8')
	reply = robot.get_response(msg['Text'])
	print('I say:'+reply)
	return reply or defaultReply

def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
