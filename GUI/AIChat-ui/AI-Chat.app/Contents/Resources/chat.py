# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("单身狗福利")
        MainWindow.resize(707, 445)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(220, 40, 281, 101))
        self.Title.setObjectName("Title")
        self.InputQue = QtWidgets.QLabel(self.centralwidget)
        self.InputQue.setGeometry(QtCore.QRect(40, 170, 131, 51))
        self.InputQue.setObjectName("InputQue")
        self.InputTxT = QtWidgets.QLineEdit(self.centralwidget)
        self.InputTxT.setGeometry(QtCore.QRect(130, 180, 431, 31))
        self.InputTxT.setObjectName("InputTxT")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(580, 180, 91, 32))
        self.send.setObjectName("send")

        self.send.clicked.connect(lambda: self.sent())

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 240, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.returnTxT = QtWidgets.QLineEdit(self.centralwidget)
        self.returnTxT.setGeometry(QtCore.QRect(140, 260, 521, 71))
        self.returnTxT.setObjectName("returnTxT")
        self.ReturnInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.ReturnInfo.setGeometry(QtCore.QRect(40, 260, 91, 71))
        self.ReturnInfo.setObjectName("ReturnInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:64pt; color:#39ff37;\">陪你聊天</span></p></body></html>"
            ))
        self.InputQue.setText(_translate("MainWindow", "你要说什么？"))
        self.send.setText(_translate("MainWindow", "发送"))
        self.ReturnInfo.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; text-decoration: underline; color:#fc563d;\">回复</span></p></body></html>"
            ))

    def sent(self):
        txt = self.InputTxT.text()
        print(txt)
        returntxt = self.txAIchat(txt, '2154831460', 'ujfCYx2dRqvfzg17')
        self.returnTxT.setText(returntxt)
        nowtime = time.strftime('%Y-%m-%d_%H:%M:%S',
                                time.localtime(time.time()))
        gaomi = '\n操作时间' + nowtime + '\n发送内容:' + txt + '\n返回内容:' + returntxt
        self.txtwebhook(
            gaomi,
            self.addticket(
                "https://oapi.dingtalk.com/robot/send?access_token=5c185ea0ae0e93ebd60b05d4704bbaff3dc120628cac9f0e1c6d3d648b0059f0",
                'SEC18480f4e0c7b5c99db6eee1b3b364569f596ce9393110d454f18fd2bac58db92'
            ), '单身狗福利AI聊天操作提示')

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
        info = requests.get(
            url='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat',
            params=params)
        answers = json.loads(info.text)
        print(answers['data']['answer'])
        return answers['data']['answer']

    def txtwebhook(self, a, webhook, keyword):  # 发送函数
        if keyword != "":
            tex = "[" + keyword + "]:" + a
        else:
            tex = a
        message = {"msgtype": "text", "text": {"content": tex}}
        # 对请求的数据进行json封装
        message_json = json.dumps(message)
        # 发送请求
        self.header = {"Content-Type": "application/json", "Charset": "UTF-8"}
        self.info = requests.post(url=webhook,
                                  data=message_json,
                                  headers=self.header)
        # 打印返回的结果
        info = self.info
        print("错误信息:", info.text)

    def addticket(self, wh, secret):  # 加签验证函数
        timestamp = int(time.time() * 1000)
        secret_enc = bytes(secret.encode('utf-8'))
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
        hmac_code = hmac.new(secret_enc,
                             string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        sign = parse.quote(base64.b64encode(hmac_code), safe='')
        # https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        return wh + "&timestamp=" + str(timestamp) + "&sign=" + sign


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())