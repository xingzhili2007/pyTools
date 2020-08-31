from MyTools import *
from MemberList import *  # Webhook地址文件
from MemberSec import *  # 密钥文件
from envValue.Dingtalk.Member import *
from envValue.TencentAI.APP import *

# 定义类()
robot = Dingtalk()
tool = Tools()
gets = Get_URLinfo()
ai = AI()
Dic = dictionary()


def Combine_English_qupeiyin(URL, store_path):
    Video_URL = gets.English_qupeiyin(URL)
    if store_path == '':
        store_path = os.getcwd() + '/Cache'
        if not os.path.exists(store_path):
            os.makedirs(store_path)
    nowtime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    nowtime = str(nowtime)
    store_path = store_path + '/' + nowtime
    os.makedirs(store_path)
    gets.download(store_path, Video_URL, '')
    print('Path:', store_path)
    '''
    if tool.nowOS() == 'win':
        os.system("explorer.exe %s" % store_path)
    elif tool.nowOS == 'mac':
        os.system("open "+store_path)
    '''
    return store_path


def Combine_baiduttsURL(text, lan, spd, toplay, store_path, filename):
    URL = tool.baiduttsURL(text, lan, spd, toplay)
    if store_path == '':
        store_path = os.getcwd() + '/Cache'
        if not os.path.exists(store_path):
            os.makedirs(store_path)
    nowtime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    nowtime = str(nowtime)
    store_path = store_path + '/' + nowtime
    if not os.path.exists(store_path):
        os.makedirs(store_path)
    # download
    if filename == '':
        filename = text + '&speed=' + str(spd) + '.mp3'
    filepath = os.path.join(store_path, filename)
    file_data = requests.get(URL, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
    print('Path:', store_path)
    return store_path


def Combine_2wm(text, store_path, filename):
    URL = tool.txt2wm(text)
    if store_path == '':
        store_path = os.getcwd() + '/Cache'
        if not os.path.exists(store_path):
            os.makedirs(store_path)

    nowtime = str(nowtime)
    store_path = store_path + '/' + nowtime
    if not os.path.exists(store_path):
        os.makedirs(store_path)
    # download
    if filename == '':
        filename = text + '.png'
    filepath = os.path.join(store_path, filename)
    file_data = requests.get(URL, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
    print('Path:', store_path)
    return store_path


def txtwebhookAuto(text, GroupName, keyW=1):
    # 检测目录中是否存在该机器人(群聊)
    try:
        webhook = DingtalkLibrary[GroupName]['Webhook']  # 如果有该机器人信息就赋值
    except:
        print('群名不存在')  # 如果没有则报错
        return False
    # 检测该机器人是否应用了加签验证
    if DingtalkLibrary[GroupName]['Sec'][0] == True:
        try:
            webhook = robot.addticket(DingtalkLibrary[GroupName]['Webhook'],
                                      DingtalkLibrary['机器人测试']['Sec'][1])  # 如果应用则加签
        except:
            print('密钥不存在')  # 如果没有则报错
            return False
    # 检测该机器人是否应用了关键字验证
    if DingtalkLibrary[GroupName]['KeyWord'][0] != 0:
        try:
            # 如果应用则选择第一个关键字
            KeyWord = DingtalkLibrary[GroupName]['KeyWord'][keyW]
        except:
            print('关键词不存在')  # 如果没有则报错
            return False
    else:
        KeyWord = ''  # 如果未应用则为空
    text = str(text)  # 格式化要发送的文字
    robot.txtwebhook(text, webhook, '', '', '', '', KeyWord)  # 发送
    return True


def AutoChat(text, app):

    appid = AILibrary[app]['APPID']
    appkey = AILibrary[app]['APPKEY']
    ai.txAIchat(text, appid, appkey)


def DicAutosort(find):

    lenfind = len(find)
    if lenfind < 1:
        print("Input Error")
    elif lenfind < 2:
        getmore = input("是否获取拓展性内容(y/n) : ")
        moreflag = False
        if getmore == 'y' or getmore == 'Y':
            moreflag = True
        Dic.findword(find, moreflag)
    elif lenfind < 3:
        Dic.findci(find)
    elif lenfind > 3:
        stat = input("输入 成语:1 歇后语:2 : ")
        if stat == '1':
            Dic.findidiom(find)
        else:
            Dic.findxhy(find)
    else:
        print("暂不支持")
