
import unittest
test_dir="./"
suit=unittest.TestLoader().discover(test_dir,pattern="*test.py")
if __name__=="__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suit)