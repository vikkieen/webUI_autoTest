from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzLogin(BasePage):
    name=(By.NAME,"username")
    pwd=(By.NAME,"password")
    buttom=(By.CSS_SELECTOR,".fastlg_l button")
    home=(By.CSS_SELECTOR,".wp .bm div.z a:nth-child(1)")
    def login(self,name,password):
        self.sendkeys(name,*self.name)
        self.sendkeys(password,*self.pwd)
        self.click(*self.buttom)
        time.sleep(6)
        if self.is_element_exists(*self.home):
            self.click(*self.home)
