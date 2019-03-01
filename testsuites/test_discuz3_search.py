from testsuites.base_testcase import *
from pageobjects.discuz_search import DiscuzSearch
from pageobjects.discuz_login import DiscuzLogin
from pageobjects.discuz_exit import DiscuzExit
from ddt import ddt,data,unpack
# import unittest

# @ddt
class Discuz3(BaseTestCase):
    # @data(["haotest","haotest"])
    # @unpack
    def test_discuz(self):
        login=DiscuzLogin(self.browser_engine.driver)
        login.login("admin","root")

        search=DiscuzSearch(self.browser_engine.driver)
        result=search.searc("haotest")
        assert "haotest" in self.browser_engine.driver.title
        # self.assertEqual(result,expect_value,msg=result)

        exit=DiscuzExit(self.browser_engine.driver)
        exit.exit()

if __name__=="__main__":
    unittest.main(verbosity=2)