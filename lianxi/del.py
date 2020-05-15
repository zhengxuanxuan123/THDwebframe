import pymysql
def del1(sql):
    db = pymysql.connect(host="106.75.210.206", port=3306, db="91thd", user="zhengxx", passwd="pmxbARq1C14",
                         charset='utf8')
    print(2)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    #sql="DELETE FROM `user` WHERE tel in ('17681842412','15732121630') and type = '0'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print(23)
    except:
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()
    print('wangcheng')

'''def del2():
    db = pymysql.connect(host="106.75.210.206", port=3306, db="91thd", user="zhengxx", passwd="pmxbARq1C14",
                             charset='utf8')
        # 使用cursor()方法获取操作游标
    cursor = db.cursor()

        # 使用execute方法执行SQL语句
    sql="DELETE FROM user_other_wechat WHERE nickname in('噫～','.')"
    try:
            # 执行sql语句
        cursor.execute(sql)
            # 提交到数据库执行
        db.commit()
    except:
            # Rollback in case there is any error
        db.rollback()

        # 关闭数据库连接
    db.close()'''
sql1="DELETE FROM `user` WHERE tel in ('17681842412','15732121630') and type = '0'"
sql2="DELETE FROM user_other_wechat WHERE nickname in('噫～','.')"
del1(sql1)
del1(sql2)
