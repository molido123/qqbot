#!/usr/bin/python3
import pymysql

def newGroup(gid):####创建新群表，如果没有就创建，没有不做改变  
    create_group_table="""
        CREATE TABLE IF NOT EXISTS gid{} (
		uid varchar(20) PRIMARY KEY,
		nickname varchar(20),
        score varchar(20),
        identity varchar(20),
        lover varchar(40)
		)ENGINE=innoDB DEFAULT CHARSET=utf8;""".format(gid)
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="********",charset="utf8",db="basic")
    cursor=conn.cursor()    
    cursor.execute(create_group_table)
    conn.commit()
    cursor.close()
    conn.close()

def newMember(uid,gid,nick,identity):
    newGroup(gid)
    insert_a_member="""INSERT IGNORE INTO gid{}(uid,nickname,score,identity) VALUES('{}','{}','0','{}');""".format(gid,uid,nick,identity)
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="*********",charset="utf8",db="basic")
    cursor=conn.cursor()
    cursor.execute(insert_a_member)
    conn.commit()
    cursor.close()
    conn.close()
    
def queryScore(gid,uid):######查询分
    try:
        sql="select * from gid{} where uid={}".format(str(gid),str(uid))
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="********",charset="utf8",db="basic")
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchone()
        cursor.close()
        conn.close()
        return result[2]
    except Exception as e:
        return "查无此人"

def alterScore(gid,uid,num):#########改变分数接口
    originScore=queryScore(gid,uid)
    afterScore=int(originScore)+num
    sql="update gid{} set score='{}' where uid='{}';".format(gid,afterScore,uid)
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="***********",charset="utf8",db="basic")
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


