from framework.Base_Page import BasePage


class BaiduPage(BasePage):
    kw = ['id','kw']  # 搜索输入框
    su = ['id','su']  # 搜索按钮

    def type_kw(self):
        self.type(self.kw, 'selenium')

    def click_su(self):
        self.click(self.su)
