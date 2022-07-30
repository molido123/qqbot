#api.py
import group
import requests
import re
import time
import json
import random

def Help():
    return "目前还没有啥功能"
def remake():
    msg="未开发"
    return msg
def keywordForGroup(message, gid, uid,nick,role,msgId):
    if(message[0:5]=="/help"):
        msg="[CQ:reply,id={}]".format(str(msgId))+Help()
        group.sendMessage(msg,gid)
    elif(message[0:7]=="/remake"):
        msg="[CQ:reply,id={}]".format(str(msgId))+remake()
        group.sendMessage(msg,gid)

