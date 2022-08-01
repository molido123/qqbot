#!/usr/bin/python3
import group
import Sql
import Remake
import ScoreSystem

def Help():
    return """/remake 看看您紫砂后能去哪\n/censor + text 自我审查\n /myself 查看自己的信用分"""


def keywordForGroup(message, gid, uid,nick,role,msgId):
    Sql.newMember(uid,gid,nick,role)###例行检查
    ScoreSystem.firstCensor(gid,uid,message)
    if(message[0:5]=="/help"):
        msg="[CQ:reply,id={}]".format(str(msgId))+Help()
        group.sendMessage(msg,gid)
    elif(message[0:7]=="/remake"):
        msg="[CQ:reply,id={}]".format(str(msgId))+Remake.remake()
        group.sendMessage(msg,gid)
    elif(message[0:7]=="/myself"):
        msg="[CQ:reply,id={}]".format(str(msgId))+ScoreSystem.queryMyself(gid,uid)
        group.sendMessage(msg,gid)
    elif(message[0:7]=="/censor"):
        msg="[CQ:reply,id={}]".format(str(msgId))+ScoreSystem.selfCensor(message[7:])
        group.sendMessage(msg,gid) 

