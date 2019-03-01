from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzReturn(BasePage):
    retu=(By.CSS_SELECTOR,"#post_reply")
    content=(By.ID,"postmessage")
    submit=(By.CSS_SELECTOR,"#postsubmit span")




    def huitie(self,content):
        self.click(*self.retu)
        self.switch_to_window(self.driver.current_window_handle)
        self.sendkeys(content,*self.content)
        self.click(*self.submit)
        time.sleep(2)

