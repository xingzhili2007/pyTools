import argparse
import re
import requests
import json
import time
'''
遇到python不懂的问题，可以加Python学习交流群：1004391443一起学习交流，群文件还有零基础入门的学习资料
'''
VERSION = "VERSION 1.0.0"


def checkUrl(url: str) -> str:
    m1 = re.match(
        "https?:\/\/pan\.baidu\.com\/s\/1([a-zA-Z0-9_\-]{5,22})", url)
    m2 = re.match(
        "https?:\/\/pan\.baidu\.com\/share\/init\?surl=([a-zA-Z0-9_\-]{5,22})", url)
    if not m1 and not m2:
        print("参数不合法")
        return False
    else:
        return True


def getKey(url: str) -> bool:
    if checkUrl(url):
        try:
            req = requests.get(f"https://node.pnote.net/public/pan?url={url}")
            code = req.status_code
            if code == 200:
                data = dict(json.loads(req.text))
                status = data.get("status", False)
                if status:
                    return data.get("access_code", "未能查询到该链接的提取码，可能原因是：该链接不需要提取码或已过期")
                else:
                    return data.get("messages", "为能查询到提取码")
            elif code == 404:
                return "不存在该链接的记录"
        except Exception as e:
            return f"请求服务器失败，错误代码:{code}"


def get_parser():
    parser = argparse.ArgumentParser()
    parser.description = "百度网盘提取码一键获取器"
    parser.add_argument('urls', metavar="urls", type=str, nargs="*",
                        help='https://pan.baidu.com/s/1ppePxCLnOIH2cvikUN8H5w')
    parser.add_argument('-v', '--version', action='store_true',
                        help='版本号')
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if args['version']:
        print(VERSION)
        return

    s_time = time.time()
    if len(args['urls']) > 1:
        for item in args["urls"][1:]:
            print(f"{item}:\r\n\t{getKey(item)}")
        e_time = time.time()
        print(f"\n\n操作完毕，总耗时：{e_time-s_time} 秒")


def main():
    command_line_runner()


main()
