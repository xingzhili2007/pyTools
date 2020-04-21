# -*- coding: utf-8 -*-
from MyTools import *
from MemberList import *  # Webhook地址文件
from MemberSec import *  # 密钥文件

# 定义类()
# ???=postmsg()
robot = postmsg()
tool = Tools()

# 循环发送(次数)
for x in range(1):
    '''
    ???.delay(是否在连续多次发送时每次都延时,延时的秒数)
    ???.txtwebhook(“*信息内容”,”*(可能需要加签)webhook地址“,@某人的手机号1,@某人的手机号2,@某人的手机号3,是否@所有人,(关键词验证法的关键词)):
    ???.linkwebhook("*题目",“*文字”,*(可能需要加签)webhook地址,“图片地址”,“*链接文件地址”)
    ???.addticket(Webhook地址,加签验证密钥)为加签验证发函数)
    ???.suo("*长网址",“*密钥:到suo.im注册申请”,“过期日期”)
    '''
    '''
    robot.delay(0, 0)
    # -----------------

    robot.txtwebhook(
        "陈怡冰 董聿泽 樊奕辰 郭曹正镐 韩冯嘉佑 韩熙康 贺彦华 李家钰 李梦寒梁士楚 刘昌桐 苏思齐 孙煜雯 王祎然 薛明睫 张博瑞 快填写",
        robot.addticket(GAllStudent(), GAllstudentSEC()),
        '', '', '', 0,
        '注意'
    )
    '''
    # -----------------
    '''
    robot.linkwebhook(
        "「薛明睫」请使用学生使用账号点击加入学生群",
        ">>>点击加入",
        G130(),
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586790249712&di=60fd4a274d4894c12d0095b67a9d4ae4&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D3009302139%2C583792013%26fm%3D214%26gp%3D0.jpg",
        "https://qr.dingtalk.com/action/joingroup?code=v1,k1,A83/oOxse4PRspKKIrGXidFeMSAmubcSxsksYHLPMV8=&_dt_no_comment=1&origin=11",
        "注意"

    )
    '''
    '''
    robot.linkwebhook(
        "董聿泽 李家钰 梁士楚 刘昌桐 苏思齐 张博瑞   请填写登记群聊学生信息,方便以后管理",
        "董聿泽 李家钰 梁士楚 刘昌桐 苏思齐 张博瑞   >>>点击进入",
        robot.addticket(GAllStudent(), GAllstudentSEC()),
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1586790249712&di=60fd4a274d4894c12d0095b67a9d4ae4&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D3009302139%2C583792013%26fm%3D214%26gp%3D0.jpg",
        "https://h5.dingtalk.com/invite-page/index.html?bizSource=____source____&corpId=dingc3fe091c7a9afa59ffe93478753d9884&inviterUid=95A40F3EE85012A96B2F679C0AD92F4C&encodeDeptId=0054DC2B53AFE745",
        ""

    )
    '''
    '''
    robot.txtwebhook(
        "大家好呀",
        robot.addticket(GtstWebhook(), GtstWebhookSEC()),
        '', '', '', 0,
        ''
    )
    '''
    '''
    robot.linkwebhook(
        '如何在钉钉群里整翻你的老师',
        '点击伽入-详情请见群公告，还有更多老司机福利等你有',
        robot.addticket(Gstd(), GstdSEC()),
        '', 'https://qr.dingtalk.com/action/joingroup?code=v1,k1,cMhTGY8ePNa3e489HXTpCeJrzODWq4gUg3ezLR0hAnc=&_dt_no_comment=1&origin=11',
        ''
    )
    '''
    print(tool.suo("https://space.dingtalk.com/s/gwHOAbltPQLOLzZQfAPaACBiMDAxZWMwYmYyNGQ0NWY3YThkOTgwOWE5NWRjZDdhYg", '', ''))
