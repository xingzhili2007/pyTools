# coding: utf-8

import requests
from bs4 import BeautifulSoup  # 从bs4这个库中导入BeautifulSoup

link = "https://m.qiqidongman.com/v/183758/0_1.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")  # 使用BeautifulSoup解析

# 找到第一篇文章标题，定位到class是"post-title"的h1元素，提取a，提取a里面的字符串，strip()去除左右空格
result = soup.find('video')
print(result)
