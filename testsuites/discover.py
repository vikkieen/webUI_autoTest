import unittest
import HTMLTestRunner
import os

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)
test_dir="./"
suit=unittest.TestLoader().discover(test_dir,pattern="*search.py")
if __name__=="__main__":
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    # runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suit)