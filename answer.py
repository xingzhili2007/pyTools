# -*- coding: utf-8 -*-
from MyTools import *
# from MemberList import *  # Webhook地址文件
# from MemberSec import *  # 密钥文件
from Combine import *
from envValue.Dingtalk.Member import *

# 定义类()
# ???=postmsg()
robot = Dingtalk()
tool = Tools()
gets = Get_URLinfo()
ai = AI()
Empty = ''

# path=/Users/lixingzhi/Downloads/mathans
for x in range(141):
    wp = 113379 + x
    p = x + 1
    url = "https://weixin.zijinshe.com/cms/upload/page/"+str(wp)+".jpg"
    gets.download("/Users/lixingzhi/Documents/en",
                  url, "八上英语P"+str(p)+"页.jpg")
