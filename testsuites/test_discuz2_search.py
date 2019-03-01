from testsuites.base_testcase import BaseTestCase
from pageobjects.delete import Delete
from pageobjects.discuz_login import DiscuzLogin
from pageobjects.discuz_exit import DiscuzExit
from pageobjects.discuz_post import DiscuzPost
from pageobjects.discuz_return import DiscuzReturn
class Discuz2(BaseTestCase):
    def test_discuz(self):
        login=DiscuzLogin(self.browser_engine.driver)
        login.login("admin","root")

        delete=Delete(self.browser_engine.driver)
        delete.shantie()
        delete.loginManage("root")
        delete.creatNew("新增的板块")
        delete.manageQiut()

        exit=DiscuzExit(self.browser_engine.driver)
        exit.exit()

        login.login("admin","root")

        post=DiscuzPost(self.browser_engine.driver)
        post.post("新版块标题","新版块内容")

        retu=DiscuzReturn(self.browser_engine.driver)
        retu.huitie("新版块的回帖")