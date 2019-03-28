# -*- coding: utf-8 -*-

import unittest
from testcase.onebasecase import BaseCase
from runner.testrunner import Runer

class KaiyuanzhongbaoCase(BaseCase):
    def setUp(cls):
        super(KaiyuanzhongbaoCase, cls).setUp()


    def tearDown(cls):
        super(KaiyuanzhongbaoCase, cls).tearDown()
        pass

    def test_a_login(self):
        res = self.apitool.post_method(api="/action/zbApi/login", data="account=xzt875@126.com&pwd=13419926370qaz")
        print res.json()["result"]["message"]
        self.dict1["uid"] = res.json()["user"]["id"]
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))

    def test_b_app_version(self):
        data = "uid=%s" % self.dict1["uid"]
        res = self.apitool.get_method(api="/action/zbApi/app_version", data=data)
        print res.json()
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
    def test_c_bd_channel(self):
        data = "uid=%s&user_id=%s&reg_id=160a3797c830cd10f8d&device_type=3&source=zb" % (self.dict1["uid"],self.dict1["uid"])
        res = self.apitool.post_method(api="/action/zbApi/bd_channel", data=data)
        print res.json()["result"]["message"]
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))
if __name__ == "__main__":
    t = Runer(u"登录功能的接口测试", u"接口测试", u"测试一")
    suite = t.load_test_from_class((KaiyuanzhongbaoCase,))
    t.run(suite)


