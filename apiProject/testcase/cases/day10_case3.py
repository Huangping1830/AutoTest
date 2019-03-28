#!encoding=utf-8
from testcase.configlog import ConfigLog
from runner.testrunner import Runer


class ApiCase(ConfigLog):
    def setUp(self):
        super(ApiCase,self).setUp()
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
    t = Runer(u"登录功能的接口测试", u"接口测试", u"测试一")
    suite = t.load_test_from_class((ApiCase,))
    t.run(suite)