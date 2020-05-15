import unittest
from framework.Base_Page import BasePage
from pageobject.idcodelogin import Idcode
from framework.readdata import ReadData
from framework.database import Dbmysql
import time
class test_login(unittest.TestCase):


    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser(self)

    def test_idcode(self):
        test_idcode = Idcode(self.driver)
        test_idcode.click_idcode()
        test_idcode.inqut_tel('15769225971')
        test_idcode.click_idma()
        test_idcode.sleep(10)
        data = Dbmysql.select("SELECT `code` FROM system_phone_msg WHERE phone='15769225971' ORDER BY id DESC LIMIT 0,1")
        test_idcode.inqut_smsRandom(data)
        test_idcode.sleep(3)
        test_idcode.click_dologin()
        test_idcode.quit()