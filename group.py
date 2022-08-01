#!/usr/bin/python3
#group.py
import json
import requests

#保存用户信息
def saveGroupUserInfo(userInfo):
    with open('userInfoOfGroup.json','w') as f:
        json.dump(userInfo,f)
#读取用户信息
def readGroupUserInfo():
    with open('userInfoOfGroup.json','r') as f:
        userInfo = json.load(f)
    return userInfo
#发送信息
def sendMessage(message,gid):
    url="http://127.0.0.1:5700/send_msg?group_id="+str(gid)+"&message="+message
    requests.get(url)
