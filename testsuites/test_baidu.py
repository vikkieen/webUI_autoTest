import unittest
from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import *
class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.browser_engine.driver)
        # home_page.get("https://baidu.com")
        home_page.search("selenium")
# if __name__=="__main__":
#     unittest.main