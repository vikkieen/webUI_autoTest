from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzPost(BasePage):
    # moren=(By.CSS_SELECTOR,".bm_c h2 a")
    fatie=(By.CSS_SELECTOR,"#newspecial img")
    title=(By.CSS_SELECTOR,"#postbox .z #subject")
    iframe=(By.TAG_NAME,"iframe")
    content=(By.TAG_NAME,"body")
    fabiao=(By.CSS_SELECTOR,"#postsubmit span")
    xinban = (By.CSS_SELECTOR, "#category_1  table tbody > tr:nth-child(2) > td:nth-child(2)  h2 a")  # 新版块下发帖
    def post(self,title,content):
        time.sleep(3)
        self.click(*self.xinban)
        time.sleep(3)
        self.click(*self.fatie)
        py = self.driver.current_window_handle
        self.sendkeys(title,*self.title)
        self.switch_to_frame(*self.iframe)
        self.sendkeys(content,*self.content)
        self.switch_to_window(py)
        self.click(*self.fabiao)
        time.sleep(2)
