# encoding:utf-8
# name:mod_db.py
'''
使用方法：1.在主程序中先实例化DB Mysql数据库操作类。
      2.使用方法:db=database()  db.fetch_all("sql")
'''
import pymysql
import pymysql.cursors
from framework.Base_Page import BasePage
from Logs.log import log1

DB = "database"
#LOGPATH = BasePage.db_getConfig('path', 'logpath') + 'database.log'
DBNAME = BasePage.db_getConfig(DB, 'dbname')
DBHOST = BasePage.db_getConfig(DB, 'dbhost')
DBUSER = BasePage.db_getConfig(DB, 'dbuser')
DBPWD = BasePage.db_getConfig(DB, 'dbpassword')
DBCHARSET = BasePage.db_getConfig(DB, 'dbcharset')
DBPORT = BasePage.db_getConfig(DB, "dbport")
logger = log1


# 数据库操作类
class database():
    # 注，python的self等于其它语言的this
    def __init__(self, dbname=None, dbhost=None):
        self._logger = logger
        # 这里的None相当于其它语言的NULL
        if dbname is None:
            self._dbname = DBNAME
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = DBHOST
        else:
            self._dbhost = dbhost

        self._dbuser = DBUSER
        self._dbpassword = DBPWD
        self._dbcharset = DBCHARSET
        self._dbport = int(DBPORT)
        self._conn = self.connectMySQL()

        if (self._conn):
            self._cursor = self._conn.cursor()

    # 数据库连接pip install mysql-connector
    def connectMySQL(self):
        conn = False
        try:
            conn = pymysql.connect(host=self._dbhost,
                                   user=self._dbuser,
                                   passwd=self._dbpassword,
                                   db=self._dbname,
                                   port=self._dbport,
                                   cursorclass=pymysql.cursors.DictCursor,
                                   charset=self._dbcharset,
                                   )
            cursor = conn.cursor()

        except Exception:
            self._logger.error("connect database failed, %s" )
            conn = False
        return conn

    # 获取查询结果集
    def fetch_all(self, sql):
        res = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception:
                res = False
                logger.warn("query database exception, %s" )
        return res

    def update(self, sql):
        flag = False
        if (self._conn):
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception:
                flag = False
                logger.warn("update database exception, %s")

        return flag
   #更新数据库中表的某几列：update login set result =%s;eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def updateByParams(self, sql, params):
        flag = False
        if (self._conn):
            try:
                self._cursor.execute(sql,params)
                self._conn.commit()
                flag = True
            except logger.Error as data:
                flag = False
                logger.warn("update database by params exception, %s" % data)
            finally:
                self.close()
        return flag


    # 关闭数据库连接
    def close(self):
        if (self._conn):
            try:
                if (type(self._cursor) == 'object'):
                    self._cursor.close()
                if (type(self._conn) == 'object'):
                    self._conn.close()
            except Exception:
                logger.warn('close database exception, %s,%s,%s')