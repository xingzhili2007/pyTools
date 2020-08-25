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

header = {"Content-Type": "application/json", "Charset": "UTF-8"}
msg = {
    "lang": "bash",
    "content": "echo Hello"
}
info = requests.post(url="http://api.pasteme.cn/", headers=header)
print(info.text);
