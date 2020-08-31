
import difflib
import json
import os
NowDir = os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + os.path.sep + ".")
def Equalrate(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def sort(lenfind):
    if lenfind < 1:
        print("Input Error")
    elif lenfind < 2:
        getmore = input("是否获取拓展性内容(y/n) : ")
        moreflag = False
        if getmore == 'y' or getmore == 'Y':
            moreflag = True
        findword(find, moreflag)
    elif lenfind < 3:
        findci(find)
    elif lenfind > 3:
        stat = input("输入 成语:1 歇后语:2 : ")
        if stat == '1':
            findidiom(find)
        else:
            findxhy(find)
    else:
        print("暂不支持")


def findci(ciyu):
    ci = json.load(open(NowDir+"/envValue/Dictionary/ci.json"))
    lenci = len(ci)
    for x in range(lenci):
        now = ci[x]
        if ci[x]['ci'] == ciyu:
            print(ci[x]['explanation'])
            return ci[x]['explanation']
    print("查无此词")
    return False


def findword(zi, getmore=False):
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


def findxhy(xhy):
    xiehouyu = json.load(open(NowDir+"/envValue/Dictionary/xiehouyu.json"))
    lenxhy = len(xiehouyu)
    for x in range(lenxhy):
        now = xiehouyu[x]["riddle"]
        if(Equalrate(now, xhy) >= 0.85):
            print("解析："+xiehouyu[x]["answer"])
            return xiehouyu[x]["answer"]
    print("查无此条")
    return False


def findidiom(cy):
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


find = input("请输入你要查询的内容 : ")
lenfind = len(find)
sort(lenfind)
