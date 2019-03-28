# -*- coding: utf-8 -*-

import unittest
from testcase.configlog import ConfigLog
from runner.testrunner import Runer

class ApiCase(ConfigLog):
    def setUp(self):
        super(ApiCase, self).setUp()

    def tearDown(self):
        super(ApiCase, self).tearDown()
        pass

    def test_alogin(self):
        res = self.apitool.post_method(api="/api", data="username=jack&password=qaz123")
        print res.json()
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))

    def test_blogin(self):
        res = self.apitool.get_method(api="/api", data="username=jack&password=qaz123")
        print res.json()
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
def Suite():
    suite = unittest.TestSuite()
    suite.addTest(ApiCase("test_blogin"))
    suite.addTest(ApiCase("test_alogin"))
    return suite

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ApiCase("test_blogin"))
    suite.addTest(ApiCase("test_alogin"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


