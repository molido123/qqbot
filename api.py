#api.py
import group
import Sql
import Remake

def Help():
    return "/remake 看看您紫砂后能去哪"


def keywordForGroup(message, gid, uid,nick,role,msgId):
    Sql.newMember(uid,gid,nick,role)
    if(message[0:5]=="/help"):
        msg="[CQ:reply,id={}]".format(str(msgId))+Help()
        group.sendMessage(msg,gid)
    elif(message[0:7]=="/remake"):
        msg="[CQ:reply,id={}]".format(str(msgId))+Remake.remake()
        group.sendMessage(msg,gid)

