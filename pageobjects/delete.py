from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class Delete(BasePage):
    moren = (By.CSS_SELECTOR,".bm_c h2 a")
    checkbox=(By.CSS_SELECTOR,".bm_c  tr:nth-child(1) .o input")
    delete=(By.CSS_SELECTOR,"#mdly p strong:first-of-type a")
    submit=(By.CSS_SELECTOR,".pns button span")
    guanli=(By.LINK_TEXT,"管理中心")
    manage_pwd=(By.NAME,"admin_password")#登录管理中心密码
    sub=(By.CSS_SELECTOR,".btn")#登录 登录管理中心提交按钮

    forum=(By.CSS_SELECTOR,".mainhd .nav li:nth-child(7) a")
    iframe = (By.TAG_NAME, "iframe")
    tianjia=(By.CSS_SELECTOR,".lastboard a")#添加新板块
    mingcheng=(By.NAME,"newforum[1][]")#新版块的名称
    tijiao=(By.ID,"submit_editsubmit")
    exit=(By.CSS_SELECTOR,".uinfo p:nth-child(1) a")#登录管理中心退出
    xinban=(By.CSS_SELECTOR,".bm_c tr:nth-child(2) h2 a")#新版块下发帖


    def shantie(self):
        self.click(*self.moren)
        self.click(*self.checkbox)
        self.click(*self.delete)
        self.click(*self.submit)
        time.sleep(2)


    def loginManage(self,password):
        self.click(*self.guanli)
        # self.driver.window_handles
        self.switch_to_window(self.driver.window_handles[1])
        self.sendkeys(password,*self.manage_pwd)
        self.click(*self.sub)
        self.click(*self.forum)


    def creatNew(self,name):
        self.switch_to_frame(*self.iframe)
        self.click(*self.tianjia)
        self.sendkeys(name,*self.mingcheng)
        self.click(*self.tijiao)
        self.switch_to_window(self.driver.window_handles[1])

    def manageQiut(self):
        self.click(*self.exit)
        self.driver.close()
        self.switch_to_window(self.driver.window_handles[0])


