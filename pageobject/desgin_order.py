from framework import Base_Page

class Desgin_order_page(Base_Page):
    desgin=['xpath','/html/body/div[2]/div[1]/div/ul[1]/li[3]/a']#找设计
    desginer=['xpatn','/html/body/div[3]/div[2]/div/ul/li[8]/div[1]/div/h4/strong/a']#郑宣宣
    def click_desgin(self):
        self.click_desgin(self.desgin)
    def clic_desginer(self):
        self.clic_desginer(self.desginer)
