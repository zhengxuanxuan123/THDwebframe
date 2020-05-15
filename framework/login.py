from testsuites.test_login import test_login
from framework.Base_Page import BasePage
from framework.readdata import ReadData
from selenium import webdriver
import unittest
data = ReadData.readcol('F:\THDwebframe\data\longin.xlsx', 'login')
#把一个列表分成两个列表（数据的处理）
usn = data[0]
psw = data[1]

#driver = test_login.setUp(webdriver)
test_login.test_logindl()