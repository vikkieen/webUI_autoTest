from abs import abs
import unittest
from ddt import ddt,data,unpack

@ddt
class AbsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test method start---------")
    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abs(self,n,expect_value):
        result=abs(n)
        self.assertEqual(result,expect_value,msg=result)
    @classmethod
    def tearDownClass(cls):
        print("teset method end-----------")
if __name__=="__main__":
    unittest.main(verbosity=2)