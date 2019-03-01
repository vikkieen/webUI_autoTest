import unittest
import HTMLTestRunner
import os
# from abs_test import AbsTestCase
# from sort_test import SortTestCase
from testsuites.test_discuz_search import Discuz
from testsuites.test_discuz2_search import Discuz2
from testsuites.test_discuz3_search import Discuz3
from testsuites.test_discuz4_search import Discuz4

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTests(unittest.makeSuite(Discuz))
suite.addTests(unittest.makeSuite(Discuz2))
suite.addTests(unittest.makeSuite(Discuz3))
suite.addTests(unittest.makeSuite(Discuz4))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")

    # runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)