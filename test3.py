import re

# 测试群聊 : "lanson"邀请"posidon"加入了群聊 (Note)
strings = '"lanson"邀请"posidon"加入了群聊'
a=strings.split('邀请')[1].split()[0].split('"')[1]
print(a)