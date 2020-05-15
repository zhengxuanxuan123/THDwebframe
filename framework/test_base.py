from selenium import webdriver
from framework.Base_Page import BasePage
dr = webdriver.Firefox()
dr.get('https://www.baidu.com/')
s = dr.window_handles
driver = BasePage(dr)
driver.maximize_window()
kw = ['id','kw']
driver.inqut(kw,'selenium+python')
driver.sleep(3)
driver.inqut(kw,'selenium')
su = ['id','su']
driver.click(su)
driver.get_img()
driver.sleep(2)
driver.get_title()
driver.quit()
