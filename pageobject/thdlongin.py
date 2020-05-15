from framework.Base_Page import BasePage

class Login(BasePage):
    #active =['class','active']#业主登录
    username =['name','username']#输入框用户名
    password=['name','password']#输入框密码
    dologin=['xpath','/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[1]/div/div[3]/button']#按钮登录
    erlogin=['xpath','///html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[1]/div/div[2]/div[3]']

    def type_username(self,value):
        self.inqut(self.username,value)
        #获取用户名元素

    def type_password(self,value):
        self.inqut(self.password,value)
        #获取密码元素

    def click_dologin(self):
        self.click(self.dologin)
        #点击登录按钮






    '''def assertEqual_er(self,value):
        self.assertE(self.erlogin,value)'''







