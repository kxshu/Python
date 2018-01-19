# coding:utf8
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

print('我我我')

itchat.auto_login()
itchat.run()
