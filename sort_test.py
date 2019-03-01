from sort import sort
import unittest
from ddt import ddt,unpack,data

@ddt
class SortTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start------")
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,n,type,expect_value):
        result=sort(n,type)
        self.assertEqual(result,expect_value,msg=result)
    @classmethod
    def tearDownClass(cls):
        print("end------------")
if __name__=="__main__":
    unittest.main(verbosity=2)