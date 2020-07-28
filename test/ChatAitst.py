import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse
import http.client
import urllib
import random
import urllib.request
import os
from bs4 import BeautifulSoup
import platform
import string


def txAIchat(TEXT, APPID, APPKEY):
    # 获得时间戳(秒级)，防止请求重放
    time_stamp = int(time.time())
    # 获得随机字符串，保证签名不被预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits,
                                      10))
    # 组合参数（缺少sign，其值要根据以下获得）
    params = {
        'app_id': APPID,
        'session': 10000,
        'question': TEXT,
        'time_stamp': time_stamp,
        'nonce_str': nonce_str
    }
    # 获得sign对应的值
    before_sign = ''
    # 对key排序拼接
    for key in sorted(params):
        before_sign += f'{key}={parse.quote(str(params[key]).encode("utf8"))}&'
    # 将应用秘钥以app_key为键名，拼接到before_sign的末尾
    before_sign += f"app_key={APPKEY}"
    # 对获得的before_sign进行MD5加密（结果大写），得到借口请求签名
    sign = hashlib.md5(before_sign.encode("utf-8")).hexdigest().upper()
    # 将请求签名添加进参数字典
    params["sign"] = sign
    '''
    API = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat?app_id=' + str(
        params['app_id']) + '&session=' + str(
            params['session']) + '&question=' + parse.quote(
                params['question']) + '&time_stamp=' + str(
                    params['time_stamp']) + '&nonce_str=' + params[
                        'nonce_str'] + '&sign=' + params['sign']
    info = requests.get(url=API)
    '''
    info = requests.get(url='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat',
                        params=params)
    answers = json.loads(info.text)
    print(answers['data']['answer'])


txAIchat('你好', '2154831460', 'ujfCYx2dRqvfzg17')
