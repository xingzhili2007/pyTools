
import zlib
import requests

url = 'https://cmts.iqiyi.com/bullet/40/00/11298454000_300_1.z'
res = requests.get(url).content
zarray = bytearray(res)
xml = zlib.decompress(zarray, 15+32).decode('utf-8')
with open('./iqiyi.xml', 'w', encoding='utf-8') as f:
    f.write(xml)
f.close()

