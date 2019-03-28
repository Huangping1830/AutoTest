# -*- coding: utf-8 -*-

import unittest
from testcase.configlog import ConfigLog
from runner.testrunner import Runer

class ApiCase2(ConfigLog):
    def setUp(self):
        super(ApiCase2, self).setUp()

    def tearDown(self):
        super(ApiCase2, self).tearDown()
        pass

    def test_alogin(self):
        res = self.apitool.post_method(api="/api", data="username=jack&password=qaz123")
        print res.json()
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))

    def test_blogin(self):
        res = self.apitool.get_method(api="/api", data="username=jack&password=qaz123")
        print res.json()
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(ApiCase)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    t = Runer(u"登录功能的接口测试",u"接口测试",u"测试一")
    suite = t.load_test_from_class((ApiCase2,))
    # suite = t.load_test_from_names(("test_alogin",))
    t.run(suite)


