# -*- coding: utf-8 -*-
from MyTools import *
#from MemberList import *  # Webhook地址文件
#from MemberSec import *  # 密钥文件
from Combine import *
from envValue.Dingtalk.Member import *

# 定义类()
# ???=postmsg()
robot = Dingtalk()
tool = Tools()
gets = Get_URLinfo()
ai = AI()
Empty = ''

#txtwebhookAuto('经过我一百年的实验，终于研制出了钉钉机器人小秘方！', '机器人测试')
#tool.baiduttsURL('水皆缥碧，千丈见底。游鱼细石，直视无碍。急湍甚箭，猛浪若奔。', '', '', '')
AutoChat('...', 'test')
