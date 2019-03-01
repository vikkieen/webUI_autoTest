import unittest
from selenium import webdriver
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    browser_engine = BrowserEngine()
    def setUp(self):
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

        self.browser_engine.open_browser()

    def tearDown(self):
        self.browser_engine.quit_browser()