#coding:utf-8
import unittest
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from testcase.configlog import ConfigLog

class ApiCase(ConfigLog):
    def setUp(self):
        super(ApiCase,self).setUp()  #super,调用父类的一个方法，用法：super(class,self).xxx
    def tearDown(self):
        super(ApiCase,self).tearDown()

    def test_b(self):
        print "b"
        res = self.apitool.get_method(api="/api", data="username=jack&passwd=qaz123")
        print self.apitool.check_error(res.json())
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
    def test_a(self):
        print "a"
        res = self.apitool.post_method(api="/api", data="username=jack&passwd=qaz123")
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ApiCase("test_b"))
    suite.addTest(ApiCase("test_a"))
    runner = unittest.TextTestRunner()
    runner.run(suite)