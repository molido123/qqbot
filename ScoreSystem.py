import encodings
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
  'Content-Type': 'application/json;charset=UTF-8',
  'groupCode': '200069'
    }
    response = requests.post(url, headers=headers, data=datas).json()
    return response
