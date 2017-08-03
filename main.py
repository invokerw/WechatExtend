#!/usr/bin/python
# -*- coding:utf-8 -*-
import itchat
import sys
import robot
import getweather
import re

reload(sys)
sys.setdefaultencoding("utf8")

#聊天模式
chat = 0
#撤回的消息
# retract = ""
retract_list = []
#撤回字典
msg_dict = {}

# 群聊消息接收 isGroupChat=True
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_chatroom(msg):
	#print(u'From:'+':'+msg['FromUserName'].encode('utf-8'))
	#print(msg['ActualNickName'].encode('utf-8')+':'+msg['Text'].encode('utf-8'))
	
	msg_id = msg['MsgId'].encode('utf8')
	msg_time = msg['CreateTime']
	msg_from = msg['ActualNickName'].encode('utf-8')
	msg_content = msg['Text'].encode('utf8')
	msg_dict.update(
		{
			msg_id:{
				"msg_from": msg_from, "msg_time": msg_time,"msg_content": msg_content
			}
		}
	)
	
	#回复
	reply = ""
	global chat
	
	defaultReply = 'I received:'+msg['Text'].encode('utf-8')
	if msg['Text'].encode('utf-8') == "天气":
		reply = getweather.get_weather(101010100)
		reply = reply + "...|..." +getweather.get_weather(101020100)
		print('I say:'+reply)
		return reply
	elif msg['Text'].encode('utf-8') == "闭嘴":
		if chat != 0:
			reply = '好的,我闭嘴'
		else:
			reply = '早就闭嘴了还要我怎样 >.<'
		chat = 0
		return reply
	elif msg['Text'].encode('utf-8') == "提问":
		if chat != 1:
			reply = '爸爸们要问什么呀~'
		else:
			reply = '我听着呢 >.<'
		chat = 1
		return reply
	elif msg['Text'].encode('utf-8') == "陪聊":
		if chat != 2:
			reply = '嘤嘤婴~主人我来啦~'
		else:
			reply = '我在这呢 >.<'
		chat = 2
		return reply
	elif msg['Text'].encode('utf-8') == "查看撤回":
		# global retract
		global retract_list
		if len(retract_list) == 0 or  msg_from != "输入不能为空":
			reply = "查看不到，实现不了 >.<"
		else :
			reply = ""
			for x in range(len(retract_list)):
				reply = reply + retract_list.pop() + "; \n"
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

@itchat.msg_register(itchat.content.NOTE,isGroupChat=True)
def send_msg_helper(msg):
	print("Note:" + msg['Content'].encode('utf8'))
	if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content'].encode('utf8')) is not None:
		old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
		old_msg = msg_dict.get(old_msg_id, {})
		msg_body = old_msg.get('msg_from') + "->撤回:" + old_msg.get('msg_content')
		msg_dict.pop(old_msg_id)
		# global retract 
		global retract_list
		# retract = msg_body
		retract_list.inset(0, msg_body)
		if len(retract_list) >= 100:
			retract_list = retract_list[0:100]


def main():
	itchat.auto_login(enableCmdQR=True,hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
