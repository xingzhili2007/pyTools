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
from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts, taxonomies, media
from wordpress_xmlrpc.compat import xmlrpc_client
NowDir = os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + os.path.sep + ".")


class Dingtalk():
    def setV(self):  # 初始化参数
        self.delaycc = True
        self.header = {"Content-Type": "application/json", "Charset": "UTF-8"}

    def txtwebhook(self, a, webhook, at1, at2, at3, atall, keyword):  # 发送函数
        self.setV()
        if keyword != "":
            tex = "[" + keyword + "]:" + a
        else:
            tex = a
        message = {
            "msgtype": "text",
            "text": {
                "content": tex
            },
            "at": {
                "atMobiles": [  # @的具体用户
                    at1, at2, at3
                ],
                "isAtAll": atall  # 此处为是否@所有人
            }
        }
        # 对请求的数据进行json封装
        message_json = json.dumps(message)
        # 发送请求
        self.info = requests.post(url=webhook,
                                  data=message_json,
                                  headers=self.header)
        # 打印返回的结果
        info = self.info
        print("错误信息:", info.text)
        self.Error = info.text
        # self.returnError()

    def linkwebhook(self, title, text, webhook, PicUrl, MsgUrl,
                    keyword):  # 发送函数
        self.setV()
        if keyword != "":
            tex = "[" + keyword + "]:" + text
        else:
            tex = text
        message = {
            "msgtype": "link",
            "link": {
                "text": tex,
                "title": title,
                "picUrl": PicUrl,
                "messageUrl": MsgUrl
            }
        }
        # 对请求的数据进行json封装
        message_json = json.dumps(message)
        # 发送请求
        self.info = requests.post(url=webhook,
                                  data=message_json,
                                  headers=self.header)
        # 打印返回的结果
        info = self.info
        print("错误信息:", info.text)

        # self.returnError()

    def addticket(self, wh, secret):  # 加签验证函数\
        self.setV()
        print("加签中")
        timestamp = int(time.time() * 1000)
        secret_enc = bytes(secret.encode('utf-8'))
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
        hmac_code = hmac.new(secret_enc,
                             string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        print("时间戳=", timestamp)
        print("签名=", sign)
        # https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        return wh + "&timestamp=" + str(timestamp) + "&sign=" + sign

    def delay(self, isevery, t):  # 延时发送
        self.setV()
        b = t
        c = t
        if isevery:
            for x in range(b):
                c -= 1
                print("Countdown:", c)
                time.sleep(1)
        elif self.delaycc:
            self.delaycc = False
            for x in range(b):
                c -= 1
                print("Countdown:", c)
                time.sleep(1)

    def returnError(self):  # 错误信息解析
        self.setV()
        error = json.loads(self.info.text)
        error = error['errmsg']
        print(error)


class Tools():
    def setV(self):
        self.lst = {'ok': '成功'}

    def suo_im(self, longw, key='5e881fa3b1b63c47b6d82fa4@92114440312e773d175743ddbb2d96e2', expDate="9999-12-31"):
        API = "http://suo.im/api.htm?url=" + \
            parse.quote(longw) + "&key=" + key + "&expireDate=" + expDate
        info = requests.get(API)
        print(info.text)
        return info.text

    def suowo(self, url, key='5e881fa3b1b63c47b6d82fa4@92114440312e773d175743ddbb2d96e2', domain=4, expDate="9999-12-31"):
        '''http://api.suowo.cn/api.htm?url=urlencode('http://weixin.qq.com')&key=5e881fa3b1b63c47b6d82fa4@92114440312e773d175743ddbb2d96e2&expireDate=2021-03-31&domain=0'''
        API = "http://api.suowo.cn/api.htm?url=" + \
            parse.quote(url)+'&key='+key+"&expireDate=" + \
            expDate+"&domain="+str(domain)
        info = requests.get(API)
        print(info.text)
        return info.text

    def trans(self, q, appid, secretKey, fromLang, toLang):

        self.setV()
        try:
            return self.lst[q]
        except:
            if appid == '':
                appid = '20200415000421256'  # 填写你的appid
            if secretKey == '':
                secretKey = '6ixIPMc0mloHoy1nbmij'  # 填写你的密钥
            if fromLang == '':
                fromLang = 'auto'  # 原文语种
            if toLang == '':
                toLang = 'zh'  # 译文语种
            httpClient = None
            myurl = '/api/trans/vip/translate'
            salt = random.randint(32768, 65536)

            sign = appid + q + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
                q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
                    salt) + '&sign=' + sign

            try:
                httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
                httpClient.request('GET', myurl)

                # response是HTTPResponse对象
                response = httpClient.getresponse()
                result_all = response.read().decode("utf-8")
                result = json.loads(result_all)

                # print(result)
                return (result['trans_result'][0]['dst'])
            except Exception as e:
                print(e)
            finally:
                if httpClient:
                    httpClient.close()

    def nowOS(self):
        nowos = platform.system()
        if nowos == "Darwin":
            return 'mac'
        elif nowos == "Windows":
            return "win"
        else:
            return 'linux'

    def baiduttsURL(self, text, lan="zh", spd=5, toplay=False):
        URL = 'https://fanyi.baidu.com/gettts?lan=' + \
            lan + '&text=' + parse.quote(text) + \
            '&spd=' + str(spd) + '&source=web'
        print(URL)
        if toplay == True:
            os.system("iina '" + URL + "'")
        return URL

    def txt2wm(self, text):
        URL = 'https://cli.im/api/qrcode/code?text=' + str(text)
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.find(class_='qrcode_plugins_img')
        print('https:' + result.attrs['src'])
        return 'https:' + result.attrs['src']


class Get_URLinfo():
    def English_qupeiyin(self, URL):
        # link格式："https://moive.qupeiyin.com/home/show/share/sharefrom/oneself/id/XXXXXXXXX"

        # 模仿浏览器
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
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

    def download(self, store_path, url, filename):
        if filename == '':
            filename = url.split("/")[-1]
        filepath = os.path.join(store_path, filename)

        file_data = requests.get(url, allow_redirects=True).content
        with open(filepath, 'wb') as handler:
            handler.write(file_data)


class AI():
    def txAIchat(self, TEXT, APPID, APPKEY):
        # 获得时间戳(秒级)，防止请求重放
        time_stamp = int(time.time())
        # 获得随机字符串，保证签名不被预测
        nonce_str = ''.join(
            random.sample(string.ascii_letters + string.digits, 10))
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
        info = requests.get(
            url='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat',
            params=params)
        answers = json.loads(info.text)
        print(answers['data']['answer'])


class WordPress():
    def sendWordpress(self, Title, Content, username, password, URL="lxzblog.xjqxz.top", status="publish", category=['未分类'], tag=['None']):
        wp = Client('http://'+URL+'/xmlrpc.php', username, password)
        post = WordPressPost()
        post.title = Title
        print("题目：", post.title)
        post.content = Content
        print("内容：", post.content)
        post.post_status = status  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
        print("状态：", post.post_status)
        post.terms_names = {
            'post_tag': tag,  # 文章所属标签，没有则自动创建
            'category': category  # 文章所属分类，没有则自动创建
        }
        print("标签", post.terms_names)
        post.id = wp.call(posts.NewPost(post))
        print("网页：", 'http://'+URL + '/?p='+str(post.id))


class dictionary():
    def Equalrate(self, str1, str2):
        return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

    def findci(self, ciyu):
        ci = json.load(open(NowDir+"/envValue/Dictionary/ci.json"))
        lenci = len(ci)
        for x in range(lenci):
            now = ci[x]
            if ci[x]['ci'] == ciyu:
                print(ci[x]['explanation'])
                return ci[x]['explanation']
        print("查无此词")
        return False

    def findword(self, zi, getmore=False):
        word = json.load(open(NowDir+"/envValue/Dictionary/word.json"))
        lenword = len(word)
        for x in range(lenword):

            now = word[x]["word"]
            nowolds = word[x]["oldword"]
            if zi == now or zi == nowolds:
                nowlist = word[x]
                print("简体字："+now)
                print("繁体字："+nowolds)
                print("笔画："+nowlist["strokes"])
                print("拼音；"+nowlist["pinyin"])
                print("部首："+nowlist["radicals"])
                print("释义："+nowlist["explanation"])
                if getmore:
                    print("拓展："+nowlist["more"])
                return nowlist
        print("查无此字")
        return False

    def findxhy(self, xhy):
        xiehouyu = json.load(open(NowDir+"/envValue/Dictionary/xiehouyu.json"))
        lenxhy = len(xiehouyu)
        for x in range(lenxhy):
            now = xiehouyu[x]["riddle"]
            if(self.Equalrate(now, xhy) >= 0.85):
                print("解析："+xiehouyu[x]["answer"])
                return xiehouyu[x]["answer"]
        print("查无此条")
        return False

    def findidiom(self, cy):
        chengyu = json.load(open(NowDir+"/envValue/Dictionary/idiom.json"))
        lenchengyu = len(chengyu)
        for x in range(lenchengyu):
            nowcy = chengyu[x]["word"]
            if nowcy == cy:
                nowlist = chengyu[x]
                print("成语："+nowcy)
                print("拼音："+nowlist["pinyin"])
                print("缩写："+nowlist["abbreviation"])
                print("释义："+nowlist["explanation"])
                print("例句："+nowlist["example"])
                print("出处："+nowlist["derivation"])
                return nowlist
        print("查无此词")
        return False
