#!encoding=utf-8
from testcase.configlog import ConfigLog
from runner.testrunner import Runer


class JuejinCase(ConfigLog):
    def setUp(self):
        super(JuejinCase,self).setUp()
    def tearDown(self):
        super(JuejinCase,self).tearDown()

    def test_b(self):
        print "b"
        res = self.apitool.post_method(api="/v1/login", data="login_type=email"
                                                            "&user=xzt875@126.com"
                                                            "&psd=13419926370"
                                                            "&client_id=de00b0cf-25be-4036-beb4-b8b3d19e190e"
                                                            "&state=8oiS9Hb96g"
                                                            "&src=android")
        print self.apitool.check_error(res.json())
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))

if __name__ == "__main__":
    t = Runer(u"登录功能的接口测试", u"接口测试", u"测试一")
    suite = t.load_test_from_class((JuejinCase,))
    t.run(suite)