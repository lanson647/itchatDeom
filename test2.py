import re
from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
my_friend = bot.friends().search('lanson')[0]
boring_group = bot.groups().search('测试群聊')[0]

# @bot.register()
# def just_print(msg):
#     # 打印消息
#     print(msg)

# @bot.register([my_friend, Group], TEXT)
# def auto_reply(msg):
#     # 如果是群聊，但没有被 @，则不回复
#     if isinstance(msg.chat, Group) and not msg.is_at:
#         return
#     else:
#         # 回复消息内容和类型
#         return '收到消息: {} ({})'.format(msg.text, msg.type)

# @bot.register(boring_group)
# def ignore(msg):
#     # 啥也不做
#     return


@bot.register(boring_group, NOTE)
def notice(msg):
        a=msg.text.split('邀请')[1].split()[0].split('"')[1]
        # 测试群聊 : "lanson"邀请"posidon"加入了群聊 (Note)
        # try:
        #     pattern = r'邀请"(.*?)"加入了群聊'
        #     r = re.compile(pattern)
        #     result = r.findall(msg)[0]
        #     # result = r.findall(msg['Content'])[0]
        #     # return(u"""
        #     #         @%s
        #     #         欢迎新同学，
        #     #         """ % result)
        #     print(result)
        # except Exception as e:
        #     print(e)

        #print(type(msg.text))
        #return boring_group.send_image('xcx.png', media_id=None)
        return boring_group.send('@img@xcx.png')
        #return '欢迎: @{} '.format(a)
        #print(a)

embed()