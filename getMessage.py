import itchat
import json


itchat.login()      # 通过二维码连接登录账号
friend_msg = itchat.get_friends(update=True)[0:]        # 获取微信好友信息

# 将微信好友信息保存起来，减少登录的次数
with open('./friend_message.json', 'w', encoding='utf-8') as file:
    json.dump(friend_msg, file, ensure_ascii=False)

file.close()

