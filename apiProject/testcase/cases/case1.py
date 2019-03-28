# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('F:/05-workspare/AutoTest/apiProject')
from testcase.configlog import ConfigLog



class ApiCase(ConfigLog):
    def setUp(self):
        super(ApiCase, self).setUp()

    def tearDown(self):
        super(ApiCase, self).tearDown()
        pass

    def test_alogin(self):
        res = self.apitool.post_method(api="/api",data="username=jack&password=qaz123")
        print res
        self.assertEqual(res.json()["code"],1,"error")
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
    def test_blogin(self):
        res = self.apitool.get_method(api="/api",data="username=jack&password=qaz123")
        print res
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))


if __name__ == "__main__":
    unittest.main()