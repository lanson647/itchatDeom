import itchat, time
from itchat.content import *
import re

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     print('%s: %s' % (msg.type, msg.text))


def note():
    @itchat.msg_register(NOTE, isGroupChat=True)
    def deal_note(msg):
        try:
            pattern = r'邀请"(.*?)"加入了群聊'
            r = re.compile(pattern)
            result = r.findall(msg['Content'])[0]
            msg.user.send(u'''@{},欢迎您的加入! 谢谢关注！
品牌工厂店直销，超级特卖，长按下图识别二维码，进入相册随意挑选哈。看中的请私信截图给@A萌萌 品牌工厂店直销'''.format(result))
            msg.user.send('@img@%s' % 'pic.jpg')
            time.sleep( 5 )
        except Exception as e:
            print(e)


if __name__ == '__main__':
    note()
    itchat.auto_login(hotReload=True)
    itchat.run()
