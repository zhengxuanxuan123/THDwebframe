from framework.Base_Page import BasePage

class Idcode(BasePage):

    idcode = ['xpath', '/html/body/div[2]/div[1]/div/div[2]/div/div[3]/ul/li[3]']  # 切换验证码登录
    dologin = ['xpath', '/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[2]/div/div[3]/button']  # 按钮登录
    tel = ['id', 'tel']  # 输入框手机号
    idma = ['xpath', '/html/body/div[2]/div[1]/div/div[2]/div/div[3]/form[2]/div/div[2]/div[2]']  # 获取验证码
    smsRandom = ['name', 'smsRandom']  # 输入框验证码

    def click_idcode(self):
        self.click(self.idcode)
        # 切换验证码登录

    def inqut_tel(self, value):
        self.inqut(self.tel, value)
        #输入框手机号码

    def click_idma(self):
        self.click(self.idma)
        #点击获取验证码

    def inqut_smsRandom(self,value):
        self.inqut(self.smsRandom,value)
        #输入框验证码

    def click_dologin(self):
        self.click(self.dologin)
        #点击登录按钮