from selenium import webdriver
cookie_dict=[]
driver = webdriver.Firefox()
#url = "http://www.91thd.com/member/login.html"
driver.get('https://bplussit3.sinosun.com:18480/mall/static/operation/channel/pages/channelaccessmgr.html')
# 获取cookie列表
cookie_list = driver.get_cookies()
print(cookie_dict)
# 格式化打印cookie
'''for cookie in cookie_list:
    cookie_dict[cookie['name']] = cookie['value']

    print(cookie_dict)'''
driver.quit()