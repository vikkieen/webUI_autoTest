from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class DiscuzSearch(BasePage):
    search=(By.CSS_SELECTOR,".scbar_txt_td input")
    button=(By.CSS_SELECTOR,"#scbar_btn")
    gaoji=(By.LINK_TEXT,"高级")
    quanwen=(By.CSS_SELECTOR,".tfm tr:nth-child(1) .pc")
    sousuo=(By.CSS_SELECTOR,".pnc strong")
    tiezi=(By.CSS_SELECTOR,".pbw:nth-child(1) h3 strong font")#搜索的帖子
    tit=(By.CSS_SELECTOR,"#thread_subject")
    def searc(self,content):
        self.sendkeys(content,*self.search)
        py=self.driver.window_handles
        self.click(*self.button)
        self.switch_to_window(self.driver.window_handles[1])
        if self.is_element_exists(*self.tiezi):
            self.click(*self.tiezi)
            self.switch_to_window(self.driver.window_handles[2])
            self.title = self.get_element_text(*self.tit)
        else:

            self.click(*self.gaoji)
            self.click(*self.quanwen)
            self.click(*self.sousuo)
            self.click(*self.tiezi)
            self.switch_to_window(self.driver.window_handles[2])
            self.title=self.get_element_text(*self.tit)
            self.switch_to_window(py)
        return self.title


