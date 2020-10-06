# -*- coding: utf-8 -*-
# Author : Xingzhi Li
# CreateDate : 2020.10.6 GMT+8 13:00
import requests
import json
header = {"Content-Type": "application/json"}


def createPasteMe(lang, content, passwd='', once="off"):
    msg = {
        "lang": lang,
        "content": content,
        "password": passwd
    }
    if once == "off":
        info = requests.post(url="http://api.pasteme.cn/",
                             headers=header, data=json.dumps(msg))
    else:
        info = requests.post(url="http://api.pasteme.cn/once",
                             headers=header, data=json.dumps(msg))
    print(info.text)
    return info.text


def getPasteMe(keyword, json="off", passwd=""):

    if passwd == "":
        url = "http://api.pasteme.cn/"+str(keyword)
    else:
        url = "http://api.pasteme.cn/"+str(keyword)+","+str(passwd)
    if json == "off":
        info = requests.get(headers=header, url=url)
    else:
        info = requests.get(headers=header, url=url+"?json=true")
    print(info.text)
    return info.text


'''
用法：

createPasteMe:创建新的Paste
    参数：
        lang----------语言[必选]( e.g "bash" )
        content-------内容[必选]( e.g "echo hello" )
        passwd--------密码[可选]( eg passwd="123456" )
        once----------是否开启阅后即焚[可选，默认once="off"]( e.g once="on" )
    完整样例
        createPasteMe("bash","echo hello","123456",once="off")
        返回 {"key":56763,"status":201} 56763即为PasteMe号码
        访问地址:https://pasteme.cn/<key> ( e.g https://pasteme.cn/56763)

getPasteMe:获取已有Paste
    参数：
        keyword---关键词[必选]( e.g "56763")
        json------是否返回json格式[可选，默认非json]( e.g json="on")
        passwd----密码[可选，默认无密码]( e.g passwd="123456")
    完整样例
        getPasteMe("56763",json="off", passwd="123456")
        返回 echo hello
        getPasteMe("56763",json="on", passwd="123456")
        返回 {"content":"echo hello","lang":"bash","status":200}
'''
