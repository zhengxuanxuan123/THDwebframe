import pymysql
from framework.Base_Page import BasePage
class Dbmysql():
    def __init__(self,put):
        self.put = put

    def select(self):
        db = pymysql.connect(host="106.75.210.206", port=3306, db="91thd", user="zhengxx", passwd="pmxbARq1C14",
                             charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(self)

        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()
        # 关闭数据库连接
        db.close()

        return data

    def updata(self):
        db = pymysql.connect(host="106.75.210.206", port=3306, db="91thd", user="zhengxx", passwd="pmxbARq1C14",
                             charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        try:
            # 执行sql语句
            cursor.execute(self)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()

