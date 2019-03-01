from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os
from selenium.webdriver.common.action_chains import ActionChains as act

logger=Logger("BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def get(self,url):
        try:
            self.driver.get(url)
            logger.info("open url")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed open the url with %s"%e)
    def quit(self):
        self.driver.quit()
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + "/screenshot/"
        rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("had take screenshot and save to folder:/scteenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed to take screenshot! %s"%e)
    def close(self):
        try:
            self.driver.close()
            logger.info("close and quit the browser")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed to quit tht browser with %s"%e)
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("successful find element")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed find element with %s"%e)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容：%s",text)
        except Exception as e:
            logger.error("failed to type in input box %s"%e)
            self.get_windows_img()
    def clear(self,*loc ):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("clear text in input box before typing")
        except Exception as e:
            logger.error("failed to clear in input box with %s"%e)
            self.get_windows_img()
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("click the link")
        except Exception as e:
            logger.error("failed to click the link with %s"%self)
            self.get_windows_img()

    def switch_to_frame(self,*loc):
        el=self.find_element(*loc)
        try:
            self.driver.switch_to.frame(el)
            logger.info("driver.switch_to.frame")
        except Exception as e:
            logger.error("failed driver.switch_to.frame %s"%el)
            self.get_windows_img()

    def switch_to_window(self,*loc):
        try:
            self.driver.switch_to.window(*loc)
            logger.info("switch_to_window")
        except Exception as e:
            logger.error("failed switch_to_window!!!")
            self.get_windows_img()

    def current_window_handle(self):
        try:
            py=self.driver.current_window_handle()
            logger.info("get current_window_handle")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed current_window_handle with %s"%e)
        return py
    def is_element_exists(self,*loc):
        flag=False
        try:
            self.find_element(*loc)
            flag=True
        except Exception as e:
            flag=False
        return flag
    def get_element_text(self,*loc):
        el=self.find_element(*loc)
        try:
            self.text=el.text
        except Exception as e:
            logger.error("failed get_element_txt")
        return self.text
    def is_page_load_complete(self):
        u"""判断web页面是不是加载完毕"""
        js = "return document.readyState"
        result = self.driver.execute_script(js)
        if result == "complete":
            return True
        else:
            return False
    def getcwd(self):
        """获得当前执行文件的系统路径"""
        return os.getcwd()
    def goto_newwindow(self):
        """跳转新的页面"""
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
    def switch_next_window(self):
        """选择新打开的浏览器窗口，主要针对链接_blank打开的新窗口选择"""
        current_window = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != current_window:
                self.driver._switch_to.window(handle)
    # def accept_alert(self):
        """处理弹出的alert框"""
        # alert = self.driver._switch_to.alert
        # print alert.text
        # self.debug_info(alert.text)
        # alert.accept()
    def move_to_element(self,*loc):
        """鼠标移动到指定元素"""
        el = self.find_element(*loc)
        act(self.driver).move_to_element(el).perform()
