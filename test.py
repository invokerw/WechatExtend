#coding=utf8
import itchat
import re

msg_dict = {}

@itchat.msg_register(itchat.content.TEXT)#,isGroupChat=True)
def ret_msg(msg):
	msg_id = msg['MsgId'].encode('utf8')
	msg_time = msg['CreateTime']
	msg_from = (itchat.search_friends(userName=msg['FromUserName']))["NickName"].encode('utf8')
	msg_content = msg['Text'].encode('utf8')
	msg_dict.update(
		{
			msg_id:{
				"msg_from": msg_from, "msg_time": msg_time,"msg_content": msg_content
			}
		}
	)

	defaultReply = 'I received: ' + msg['Text']
	return defaultReply
@itchat.msg_register(itchat.content.NOTE)
def send_msg_helper(msg):
	print(msg['Content'].encode('utf8'))
	if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content'].encode('utf8')) is not None:
		print("xxx")
		old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
		old_msg = msg_dict.get(old_msg_id, {})
		msg_body = old_msg.get('msg_from') + " 撤回->" + old_msg.get('msg_content')
		msg_dict.pop(old_msg_id)
		print(msg_body)
def main():
	itchat.auto_login(enableCmdQR=True)
	itchat.run()

if __name__ == '__main__':
	main()
