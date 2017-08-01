#coding=utf8
import itchat


@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def ret_msg(msg):
	defaultReply = 'I received: ' + msg['Text']
	return defaultReply
def main():
	itchat.auto_login(enableCmdQR=True)
	itchat.run()

if __name__ == '__main__':
	main()
