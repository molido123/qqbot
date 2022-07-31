import pymysql

def newGroup(gid):
    create_group_table="""
        CREATE TABLE IF NOT EXISTS gid{} (
		uid varchar(20) PRIMARY KEY,
		nickname varchar(20),
        score varchar(20),
        identity varchar(20),
        lover varchar(40)
		)ENGINE=innoDB DEFAULT CHARSET=utf8;""".format(gid)
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="Hua114514*",charset="utf8",db="basic")
    cursor=conn.cursor()    
    cursor.execute(create_group_table)
    conn.commit()
    cursor.close()
    conn.close()

def newMember(uid,gid,nick,identity):
    newGroup(gid)
    insert_a_member="""INSERT IGNORE INTO gid{}(uid,nickname,score,identity) VALUES('{}','{}','0','{}');""".format(gid,uid,nick,identity)
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="*******",charset="utf8",db="basic")
    cursor=conn.cursor()
    cursor.execute(insert_a_member)
    conn.commit()
    cursor.close()
    conn.close()
    


