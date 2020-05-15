import pymysql
from framework.Base_Page import BasePage


def select(sql):
    db = pymysql.connect(host="106.75.210.206", port=3306, db="91thd", user="zhengxx", passwd="pmxbARq1C14",
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute(sql)

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    print(data)

    #return data
a ="select mid from user where tel='15769225975'"
select(a)