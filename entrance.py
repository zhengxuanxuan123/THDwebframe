'''import testsuites.test_baidu
import testsuites.test_baidu_new
import unittest
import getcwd
import os
import HTMLTestRunnerCN
from framework import my_email

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testsuites.test_baidu.test_baidu('test_baisu'))
    suite.addTest(testsuites.test_baidu_new.test_baidu_new('test_new'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'report/baiduUI自动化测试报告.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='thdUI自动化测试报告',
        description='报告中描述部分',
        tester='测试者'
    )
    runner.run(suite)
    my_email.mail()
    fp.close()'''

#coding=utf-8
import unittest
import HTMLTestRunner
import time
import getcwd
import os
import HTMLTestRunnerCN
from framework import my_email
def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='F:\\THDwebframe\\testsuites'
    u'''定义 discover 方法的参数'''
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',
    top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print (test_case)
        testunit.addTests(test_case)
    return testunit
now = time.strftime("%Y-%m-%d %H_%M_%S")
path = getcwd.get_cwd()
file_path = os.path.join(path, 'report/thdUI自动化测试报告'+now+'.html')
fp = open(file_path, 'wb')
runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='thdUI自动化测试报告',
        description='报告中描述部分',
        tester='测试者'
    )
if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    alltestnames = creatsuite()
    runner.run(alltestnames)
    my_email.mail()
    fp.close()