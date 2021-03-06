# -*- coding: utf-8 -*-
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
import difflib

# Paste Your Code Under
Code='\
#include<iostream> \
using namespace std;\
int a, b;\
int main(){\
    cin>>a>>b;\
    cout<<a+b;\
    return 0;\
}\
'



login = r'%5B%22xingzhili2007%22%2C%22597aca5b6798e6db41204847bea4e2cb%22%5D';# 登录cookie
language = "cpp"
problemnum="1"
header = {"Charset": "UTF-8", "cookie": "login="+login}

body = {"language":language,"code": Code}

info=requests.post("http://sdfzoj.zhaojinxi.top/problem/" + \
                   problemnum+"/submit", headers=header, data=json.dumps(body))

print (info.text);

#print(body)
