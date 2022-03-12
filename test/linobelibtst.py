import requests
import time
from bs4 import BeautifulSoup
from opencc import OpenCC
import sys

if len(sys.argv) != 2:
    print('error')
    sys.exit()

web = sys.argv[1]
content = requests.get(web)
soup = BeautifulSoup(content.text, "html.parser")
soup_title = soup.findAll('h1')

print(content.text)
title = soup_title[0].text
cc = OpenCC('s2tw')
title = cc.convert(title)

soup_list = []
soup_list.append(soup.findAll('div', class_="content"))

web = web[0:(len(web)-5)]

i = 2
while True:
    time.sleep(1)
    content = requests.get(web+'_'+str(i)+'.html')
    soup = BeautifulSoup(content.text, "html.parser")
    soup_text = soup.findAll('div', class_="content")
    if soup_text[0].text == '\n\n':
        break
    soup_list.append(soup_text)
    i = i+1

text = ''
for i in soup_list:
    text += i[0].get_text(separator="\n")
text = text.replace('（本章未完）', '')
text = cc.convert(text)

f = open(title+'.txt', 'w', encoding="utf-8")
f.write(text)
f.close()
