#!/usr/bin/python3
import Sql
import requests
import json
def esu(text):
    url = "http://localhost:4000/sensitive"
    datas = {"txt":text}
    datas = json.dumps(datas) 
    datas = datas.encode("utf-8")
    headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Content-Type': 'application/json;charset=UTF-8'
    }
    response = requests.post(url, headers=headers, data=datas).json()
    return response

def defineScore(text):
  data=esu(text)
  if(data.get("regularResult")!="非广告文本"):
    return -1
  elif(int(data.get("score"))==0):
    return 1
  else:
    return -int(data.get("score"))

def queryMyself(gid,uid):
  result=Sql.queryScore(gid,uid)
  if(result=="查无此人"):
    return "此人也许活着，但在我的心里他不存在"
  if(int(result)>=0):
    msg="您的文明分数是「{}」，还挺文明的。".format(result)
    return msg
  elif(-99<int(result)<0):
    msg="您的文明分数是「{}」，不是很文明，再接再厉捏".format(result)
    return msg
  elif(int(result)<=-100):
    msg="您的文明分数是「{}」，可以裱起来挂在地狱城门上".format(result)
    return msg
  elif(int(result)>100):
    msg="您的文明分数是「{}」，您就是！我的圣人啊".format(result)
    return msg
  
def firstCensor(gid,uid,text):
  score=defineScore(text)
  Sql.alterScore(gid,uid,score)


def selfCensor(text):
  data=esu(text)
  if(data.get("regularResult")!="非广告文本"):
    msg="您发送的文本为广告，类型「{}」，信用分变更「{}」，广告狗给我滚".format(data.get("regularResult"),-1)
    return msg
  if(int(data.get("score"))==0):
    msg="这条消息没什么问题，✅"
    return msg
  else:
    msg="这条消息包含敏感词，敏感等级「{}」，信用分变更「{}」，和谐过的文本为「{}」".format(data.get("grade"),-data.get("score"),data.get("txtReplace"))
    return msg
  




  
