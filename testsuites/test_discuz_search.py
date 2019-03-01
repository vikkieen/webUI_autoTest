import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_login import DiscuzLogin
from pageobjects.discuz_post import DiscuzPost
from pageobjects.discuz_return import DiscuzReturn
from pageobjects.discuz_exit import DiscuzExit
class Discuz(BaseTestCase):
    def test_discuz_login(self):
        login=DiscuzLogin(self.browser_engine.driver)
        login.login("admin","root")


        post=DiscuzPost(self.browser_engine.driver)
        post.post("标题","hello word")


        retu=DiscuzReturn(self.browser_engine.driver)
        retu.huitie("这是回帖内容")

        exit=DiscuzExit(self.browser_engine.driver)
        exit.exit()
