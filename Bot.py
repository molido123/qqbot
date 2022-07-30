from unittest.mock import NonCallableMagicMock
from flask import Flask, request
import requests
import api
app = Flask(__name__)

'''监听端口，获取QQ信息'''
@app.route('/', methods=["POST"])
def post_data():
    '下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
    if request.get_json().get('message_type')=='private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.keywordForPerson(message,uid)
    if request.get_json().get('message_type')=='group':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        nick=request.get_json().get('sender').get('nickname')
        role=request.get_json().get('sender').get('role')
        msgId=request.get_json().get("message_id")
        print(request.get_json())
        api.keywordForGroup(message, gid, uid,nick,role,msgId)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
