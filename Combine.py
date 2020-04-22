from MyTools import *
from MemberList import *  # Webhook地址文件
from MemberSec import *  # 密钥文件

# 定义类()
robot = postmsg()
tool = Tools()
gets = Get_URLinfo()


def Combine_English_qupeiyin(URL, store_path):
    Video_URL = gets.English_qupeiyin(URL)
    if store_path == '':
        default = os.getcwd()+'/Cache'
        if not os.path.exists(default):
            os.makedirs(default)
        store_path = default
    gets.download(store_path, Video_URL)
