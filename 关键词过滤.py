#!/usr/bin/python
# -*- coding:utf-8 -*-

import ahocorasick
A = ahocorasick.Automaton()

A.add_word('最优秀', (0, '最优秀'))
A.add_word('最佳', (0, '最佳'))
A.add_word('最好', (0, '最好'))
# A.add_word('c', (1, 'c'))

# if 'hahhahah' in  A :
#     print("TRUE")
# else:
#     print("TRUE")


A.make_automaton()
# a=0
# for item in A.iter("_hahhahahhahhahhaheeeee_"):
#     a=a+1
 

# import  mysql.connector
# config = {
#     'host': '121.42.33.20',
#     'user': 'mysql_htmp',
#     'password': 'htmp@MySQL',
#     'port': 8306,
#     'database': 'htmp',
#     'charset': 'utf8'
# }
# conn=mysql.connector.connect(**config)
# cursor=conn.cursor()
# cursor.execute('select * from wx_users where id in(%s,%s)',('10','11',))
# value=cursor.fetchall()
# for item in value:
#     print(item)
# cursor.close()
# conn.close()


# from sqlalchemy import Column,String,create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# Base=declarative_base()
# class User(Base):
#     __tablename__='wx_users'
#     id=Column(String(20),primary_key=True)
#     nickname=Column(String(200))
# engine=create_engine('mysql+mysqlconnector://mysql_htmp:htmp@MySQL@121.42.33.20:8306/htmp?charset=utf8')

# DBSession = sessionmaker(bind=engine)
# session=DBSession()
# user=session.query(User).filter(User.id=='10').one()
# with open('test.txt','w') as f:
#     f.writeline(user.nickname)
# session.close()



# -*- coding:utf-8 -*-

import pymssql

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            pass
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            pass
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

# 独特的语言体系


ms = MSSQL(host="219.148.37.182",user="tyjzk_sa",pwd="wsdckyx7.4",db="new_foodszs")
for i in range(10):
    reslist = ms.ExecQuery("select top 1 id,content from Food_News  where sxstate=0")
    # print(reslist)
    strs=""
    if reslist is not None:
        a=0
        
        for item in A.iter((reslist[0][1]).encode('utf-8')):
            a=a+1
            print("a:",a)
            strs+=str(item[1][1])+","
        
        ms.ExecNonQuery("update Food_News set sxstate=1,sxkeywords='"+strs+"' where id="+str(reslist[0][0]))

# for i in reslist:
#     print i

# newsql="update webuser set name='%s' where id=1"%u'测试'
# print newsql
# ms.ExecNonQuery(newsql.encode('utf-8'))