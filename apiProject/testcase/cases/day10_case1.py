import unittest
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from commonTools.apiTools import ApiTools

class ApiCase(unittest.TestCase):
    def setUp(self):
        print("start")
        self.t = ApiTools()
    def tearDown(self):
        print("end")
    
    def test_b(self):
        print("b")
        res = self.t.get_method(api="/api", data="username=jack&passwd=qaz123")
        print(self.t.check_error(res.json()))
    def test_a(self):
        print("a")
        res = self.t.post_method(api="/api", data="username=jack&passwd=qaz123")
        print(self.t.check_error(res.json()))
if __name__ == "__main__":
    unittest.main()

