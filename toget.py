# coding: utf-8

import requests
import random
import time
from bs4 import BeautifulSoup  # 从bs4这个库中导入BeautifulSoup


def getfrom_qupeiyin(URL):
    # link格式："https://moive.qupeiyin.com/home/show/share/sharefrom/oneself/id/XXXXXXXXX"

    # 模仿浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    # 获取HTML源码
    r = requests.get(URL, headers=headers)
    # 使用BeautifulSoup（毒鸡汤）解析
    soup = BeautifulSoup(r.text, "html.parser")

    # 找到视频地址
    result = soup.find('video')

    # 打印
    print('FindVideoURL:Successfully \nResult=', result.attrs['src'])

    # 返回结果
    return result.attrs['src']
