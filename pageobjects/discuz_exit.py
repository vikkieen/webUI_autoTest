from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzExit(BasePage):
    quit=(By.LINK_TEXT,"退出")
    def exit(self):
        self.click(*self.quit)