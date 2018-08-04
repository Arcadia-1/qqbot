# -*- coding: utf-8 -*-

# 插件加载方法：
# 1. 启动 qqbot 
# 2. 将本文件保存至 ~/.qqbot-tmp/plugins 目录 （或 c:\user\xxx\.qqbot-tmp\plugins ）
# 3. 在命令行窗口输入： qq plug sample

def onQQMessage(bot, contact, member, content):
    if '开车' in content:
        bot.SendTo(contact, '假的，这你也信')
		
    if 'zzs' in content:
        bot.SendTo(contact, 'mua!~')
		
    if 'txt' in member.name:
        bot.SendTo(contact, '甜心！~')
		
    if '凛冬已至' in member.name:
        bot.SendTo(contact, '凛冬未至')
		
    if contact.name == '17没有发动机':
        if content != member.name+'!~':
            bot.SendTo(contact, member.name+'!~')
		
    if contact.name == 'qqbot测试':
        if content != 'nbiujbuijob':
            bot.SendTo(contact, member.name)
    
    #if ('2018' in contact.name) and ('-' in member.name):
        #bot.SendTo(contact, '学妹！')
    print(member.name)