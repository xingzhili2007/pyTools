import requests
import os
import multiprocessing
from bs4 import BeautifulSoup
from MyTools import *
# from MemberList import *  # Webhook地址文件
# from MemberSec import *  # 密钥文件
from Combine import *
from envValue.Dingtalk.Member import *
path='lll'
# 定义类()
# ???=postmsg()
robot = Dingtalk()
tool = Tools()
gets = Get_URLinfo()
ai = AI()
Empty = ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1'}


def saveFile(url, path):
    response = requests.get(url, headers=headers)
    with open(path, 'wb') as f:
        f.write(response.content)
        f.flush()


def getWebsite(url):
    site = requests.get(url, headers=headers)
    content = site.text
    soup = BeautifulSoup(content, 'lxml')
    divs = soup.find_all(class_='gdtm')
    title = soup.h1.get_text()
    page = 0
    i = 0
    for div in divs:
        picUrl = div.a.get('href')
        page = page+1
        print('Saving file '+'Path'+str(page)+'.jpg')
    
        gets.download('/Users/lixingzhi/Downloads/comic/Path',getPicUrl(picUrl), str(page)+'.jpg')
        i = i+1
        
            
    print('Finished downloading '+str(page) +
        ' files,'+str(i)+' of them are successful')
    menu()


def getPicUrl(url):
    site_2 = requests.get(url, headers=headers)
    content_2 = site_2.text
    soup_2 = BeautifulSoup(content_2, 'lxml')
    imgs = soup_2.find_all(id="img")
    for img in imgs:
        picSrc = img['src']
        return picSrc


def menu():
    url = input('Please enter the url\n')
    if (url.find('https://e-hentai.org/g/') != -1):
        print('--OK,getting information--')
        try:
            site = requests.get(url, headers=headers)
            print("ok")
            content = site.text
            print("ok")
            soup = BeautifulSoup(content, 'lxml')
            print("ok")
            divs = soup.find_all(class_='gdtm')
            print("ok")
            title = str(soup.h1.get_text())
            print("ok")
            page = 0
            print("ok")
            for div in divs:
                print("ok", div)
                page = page+1
        except:
            print('Wrong!Please try again!!!')
            menu()
        else:
            print('The comic name is '+title+',it has ' +
                str(page)+' page,start downloading!!!')
            
            #os.mkdir('~/Downloads/comic/'+'Path')
            getWebsite(url)
    else:
        print('Oh,it is not an e-hentai comic url,please enter again\n')
        menu()


menu()
