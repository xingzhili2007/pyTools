from MyTools import *
from myMemberList import *  # Webhook地址文件
from myMemberSec import *  # 密钥文件

# 定义类()
robot = Dingtalk()
tool = Tools()
gets = Get_URLinfo()


def Combine_English_qupeiyin(URL, store_path):
    Video_URL = gets.English_qupeiyin(URL)
    if store_path == '':
        store_path = os.getcwd()+'/Cache'
        if not os.path.exists(store_path):
            os.makedirs(store_path)
    nowtime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    nowtime = str(nowtime)
    store_path = store_path + '/'+nowtime
    os.makedirs(store_path)
    gets.download(store_path, Video_URL)
    print('Path:', store_path)
    '''
    if tool.nowOS() == 'win':
        os.system("explorer.exe %s" % store_path)
    elif tool.nowOS == 'mac':
        os.system("open "+store_path)
    '''
    return store_path
