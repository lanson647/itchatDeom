import itchat, time
from itchat.content import *
import re


@itchat.msg_register(NOTE, isGroupChat=True)
def deal_note(msg):
    m = re.search('加入',msg.Content)
    #直接截取第三个引号后的字符串
    result = msg.text.split('"')[3]
    if m is not None:
        msg.user.send(u'''@{},欢迎您的加入! 谢谢关注！
品牌工厂店直销，超级特卖，长按下图识别二维码，进入相册随意挑选哈。看中的请私信截图给@A萌萌 品牌工厂店直销'''.format(result))
        msg.user.send('@img@%s' % 'xcx.png')
    else:
        print("失败了")


itchat.auto_login(hotReload=True)
itchat.run()
