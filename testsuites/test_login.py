import unittest
from framework.Base_Page import BasePage
from pageobject.thdlongin import Login
from framework.readdata import ReadData
data = ReadData.readcol('F:\THDwebframe\data\longin.xlsx', 'login')
#把一个列表分成两个列表（数据的处理）
usn = data[0]
psw = data[1]
erlogin=['xpath','/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[1]/div/div[2]/div[3]']
username=['xpath','/html/body/nav/div/ul[1]/li[2]/span']
userre = ['xpath','/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[1]/div/div[1]/div[2]']
passw=['xpath','/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[1]/div/div[2]/div[3]']
userlack=['xpath','/html/body/div[2]/div[1]/div/div[2]/div/div[4]/span']
class test_login(unittest.TestCase):


    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser(self)


    def test_logindl(self):
        test_logindl =Login(self.driver)
        test_logindl.type_username(usn[0])
        test_logindl.type_password(psw[0])
        test_logindl.click_dologin()
        self.assertEqual('您好，欢迎来到THD庭好的共享家装平台！', test_logindl.find_element(username).text)
        test_logindl.quit()


    def test_login_namenull(self):
        test_login_namenull = Login(self.driver)
        test_login_namenull.type_username(usn[4])
        test_login_namenull.type_password(psw[4])
        test_login_namenull.click_dologin()
        self.assertEqual('输入密码 不得小于6位', test_login_namenull.find_element(erlogin).text)
        test_login_namenull.quit()

    def test_login_userre(self):
        test_login_userre = Login(self.driver)
        test_login_userre.type_username(usn[1])
        test_login_userre.type_password(psw[1])
        test_login_userre.click_dologin()
        self.assertEqual('请输入用户名/手机号',test_login_userre.find_element(userre).text)
        test_login_userre.quit()

    def test_login_passwordnull(self):
        test_login_psswordnull= Login(self.driver)
        test_login_psswordnull.type_username(usn[2])
        test_login_psswordnull.type_password(psw[2])
        test_login_psswordnull.click_dologin()
        self.assertEqual('请输入密码',
            test_login_psswordnull.find_element(passw).text)
        test_login_psswordnull.quit()

    def test_login_userlack(self):
        test_login_userlack = Login(self.driver)
        test_login_userlack.type_username(usn[3])
        test_login_userlack.type_password(psw[3])
        test_login_userlack.click_dologin()
        self.assertEqual('账号或密码不正确！',test_login_userlack.find_element(userlack).text)
        test_login_userlack.quit()

