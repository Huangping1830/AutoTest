# -*- coding: utf-8 -*-
import time
import unittest

from casesTools.basecase import BaseCase
from appProject.util.resultTools import createReport


class LoginCase(BaseCase):
    def setUp(self):
        super(LoginCase, self).setUp()

    def tearDown(self):
        super(LoginCase, self).tearDown()

    def test_run(self):
        time.sleep(2)
        self.commonTools.saveScreenshot()
        time.sleep(3)
        self.commonTools.saveScreenshot()
        x_start,y_start,x_end,y_end = self.commonTools.swipeLocation("//android.widget.RelativeLayout")
        self.commonTools.swipe(x_start,y_start,x_end,y_end,500)
        self.commonTools.waitForElement("net.oschina.app:id/btn_introduce",2)
        self.commonTools.clickElement("net.oschina.app:id/btn_introduce")
        self.commonTools.clickElement("net.oschina.app:id/tv_next")
        self.commonTools.clickElement("net.oschina.app:id/tv_next_english")
        self.commonTools.clickElement("net.oschina.app:id/tv_sure")
        self.commonTools.waitForElement("我的",2)
        self.commonTools.clickElement("我的")
        self.commonTools.clickElement("点击头像登录")
        self.commonTools.sendKeys("net.oschina.app:id/et_login_username","18201147054")
        self.commonTools.sendKeys("net.oschina.app:id/et_login_pwd","HP19900114")
        self.commonTools.clickElement("net.oschina.app:id/bt_login_submit")
        self.commonTools.waitForElement("飞天PP")
        self.commonTools.clickElement("综合")


        time.sleep(3)
        self.logger.info(''.join([self.log_cur_name(), " - run : ", "点击成功"]))

def Suite():
    suiteTest  = unittest.TestSuite()
    suiteTest.addTest(LoginCase("test_run"))
    return suiteTest
if __name__ == "__main__":
    # unittest.main()
    createReport(Suite(),u"开源中国测试测试用例",u"开源中国登陆测试用例")