'''
存储模版:
Library:
    #群聊标识符
    'GroupName': {
        #Webhook地址:
        "Webhook":#类别名称
        "https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXXX"#类别内容
        ,#分隔符
        #机器人加签密钥:
        "Sec": [],#类别名称:Sec-类别内容_格式:列表[bool(是否需要加签验证),str(密钥)]
        "KeyWord": []#类别名称:KeyWord-类别内容_格式:列表[int(关键词的个数),str(关键词1),str(关键词2)......]
    }
'''
DingtalkLibrary = {
    #群聊标识符
    '一年级12班(130班)': {
        #Webhook地址:
        "Webhook":#类别名称
        "https://oapi.dingtalk.com/robot/send?access_token=4831e8e3bdfdec5129e6d642b10838e58abec5e480500a872a3d88a97d973362"#类别内容
        ,#分隔符
        #机器人加签密钥:
        "Sec": [False],#类别名称:Sec-类别内容_格式:列表[bool(是否需要加签验证),str(密钥)]
        "KeyWord": [4, '信息', '提示', '警告', '注意']#类别名称:KeyWord-类别内容_格式:列表[int(关键词的个数),str(关键词1),str(关键词2)......]
    }

    ,#分隔符

    #群聊标识符
    '一年级12班(130班)学生': {
        #Webhook地址:
        "Webhook":#类别名称
        "https://oapi.dingtalk.com/robot/send?access_token=bfde62537453645a25574567f1c51a8b6db520c146ac66327100c7656771e94e"  #类别内容
        ,#分隔符
        "Sec": [
            True,#类别名称:Sec
            'SEC836ce2bd8032e17d918cfb54a57345dc68ddc741be88e5d370f1e6568b1f9086'#类别内容_格式:列表[bool(是否需要加签验证),str(密钥)]
        ],
        "KeyWord": [False]#类别名称:KeyWord-类别内容_格式:列表[int(关键词的个数),str(关键词1),str(关键词2)......]
    },

    #群聊标识符
    '机器人测试': {
        #Webhook地址:
        "Webhook":#类别名称
        "https://oapi.dingtalk.com/robot/send?access_token=5c185ea0ae0e93ebd60b05d4704bbaff3dc120628cac9f0e1c6d3d648b0059f0"#类别内容
        ,#分隔符
        #机器人加签密钥:
        "Sec": [True,'SEC18480f4e0c7b5c99db6eee1b3b364569f596ce9393110d454f18fd2bac58db92'],#类别名称:Sec-类别内容_格式:列表[bool(是否需要加签验证),str(密钥)]
        "KeyWord": [False]#类别名称:KeyWord-类别内容_格式:列表[int(关键词的个数),str(关键词1),str(关键词2)......]
    }
}
