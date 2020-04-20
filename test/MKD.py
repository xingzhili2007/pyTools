
        
message ={

    "msgtype": "markdown",
    "markdown": 
        {
        "title":"杭州天气",
        "text": "#### 杭州天气 \n" +
            "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
            "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
            "> ###### 10点20分发布 [天气](https://www.seniverse.com/) \n"
        },
    "at": 
    {
        "atMobiles": 
        [
            
        ], 
        "isAtAll": false
    }

}


#构建请求头部
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}

#对请求的数据进行json封装
message_json = json.dumps(message)
#发送请求

info = requests.post(url=webhook,data=message_json,headers=header)
#打印返回的结果
print("错误信息:",info.text)
self.Error=info.text