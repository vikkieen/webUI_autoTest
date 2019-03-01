from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_login import DiscuzLogin
from pageobjects.discuz_vote import DiscuzVote

class Discuz4(BaseTestCase):
   def test_discuz(self):
       login=DiscuzLogin(self.browser_engine.driver)
       login.login("admin","root")

       vote=DiscuzVote(self.browser_engine.driver)
       vote.fabiao("投票标题","Axuanze","Bxuanze","Cxuanze")
       vote.toupiao()
       vote.getName()
       vote.getTitle()
