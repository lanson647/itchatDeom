import itchat, time
from itchat.content import *
import re

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
#     itchat.send('@img@%s' % 'xcx.png')

# @itchat.msg_register(itchat.content.SHARING)
# def print_content(msg):
#     # print(msg)
#     return(msg)

# @itchat.msg_register(itchat.content.SHARING)
# def print_content(msg):
#     return msg['Content']



# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('@img@%s' % 'xcx.png')


itchat.auto_login()
itchat.run()


# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     print('%s: %s' % (msg.type, msg.text))


# def note():
#     @itchat.msg_register(NOTE, isGroupChat=True)
#     def deal_note(msg):
#         try:
#             pattern = r'邀请"(.*?)"加入了群聊'
#             r = re.compile(pattern)
#             result = r.findall(msg['Content'])[0]
#             # itchat.send('@img@%s' % 'xcx.png')
#             return(u"""
#                     @%s
#                     欢迎新同学，
#                     """ % result)
#         except Exception as e:
#             print(e)


# if __name__ == '__main__':
#     note()
#     itchat.auto_login()
#     itchat.run()
