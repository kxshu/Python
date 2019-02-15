# coding: utf-8
from wxpy import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

#导入wxpy模块的全部内容
bot=Bot(cache_path=True, console_qr=1)
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot.groups(update=True, contact_only=False)
#微信登陆后，更新微信群列表（包括未保存到通讯录的群）
my_groups=bot.groups().search(u'成都互联网')
#找出名字包括“铲屎官”的群。假设我们有2个微信群，分别叫“铲屎官1群”、“铲屎官2群”。如果有3个或以上的铲屎群，上面这句代码也能全部找出来，并在后面的代码中实现多群同步。
my_groups[0].update_group(members_details=True)
#更新“铲屎官1群”的成员列表信息
my_groups[1].update_group(members_details=True)
#更新“铲屎官2群”的成员列表信息
@bot.register(my_groups, except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
def sync_my_groups(msg):
    my_name='【'+group.name+'】'+msg.member.name+':'
    #给转发的消息加上前缀，显示群成员名字和冒号。群成员名字从备注、群昵称、微信昵称里面按顺序自动获取。
    sync_message_in_groups(msg, my_groups, prefix=my_name) 
    #同步“铲屎官1群”和“铲屎官2群”的消息。包括文字、图片、视频、语音、文件、分享、普通表情、地图等。
bot.file_helper.send('sync!')
#向机器人的文件传输助手发送消息“Hello”
bot.join() 
#堵塞线程，让机器人保持运行 
