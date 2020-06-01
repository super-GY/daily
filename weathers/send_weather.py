#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"


import itchat
from weathers import weather

itchat.auto_login(hotReload=False)
friends_list = itchat.get_friends(update=True)
name = itchat.search_friends(name=u'冬小麦')
Aying = name[0]["UserName"]

message_list = weather.main('海淀')  # 发送天气情况
itchat.send(message_list, Aying)


"""
Your wechat account may be LIMITED to log in WEB wechat, error info:
<error><ret>1203</ret><message>为了你的帐号安全，此微信号已不允许登录网页微信。
你可以使用Windows微信或Mac微信在电脑端登录。Windows微信下载地址：https://pc.weixin.qq.com 
 Mac微信下载地址：https://mac.weixin.qq.com</message></error>

"""