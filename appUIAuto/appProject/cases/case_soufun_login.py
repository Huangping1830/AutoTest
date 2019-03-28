# -*- coding: utf-8 -*-
from __future__ import absolute_import

import time
import unittest
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from util.commonTools import CommonTools


class Login_Logout(unittest.TestCase):
    def setUp(self):
        self.commonTools =CommonTools("configs.conf")
        self.commonTools.initDriver()
    def tearDown(self):
        time.sleep(5)
        # self.commonTools.quitDriver()
    def test_run(self):
        time.sleep(3)
        self.commonTools.saveScreenshot()
        time.sleep(3)
        self.commonTools.saveScreenshot()
        # self.commonTools.waitForElement("com.soufun.app:id/iv_more", 3)
        # self.commonTools.clickElement("com.soufun.app:id/iv_more")
        time.sleep(3)
        self.commonTools.saveScreenshot()
        # x_start, y_start, x_end, y_end = self.commonTools.swipeLocation("//android.widget.RelativeLayout[@resource-id=\"com.soufun.app:id/rl_myhead_loginin\"]/android.widget.LinearLayout[1]")
        # self.commonTools.swipe(x_start, y_start, x_end, y_end, 500)
        # self.commonTools.sendKeys("com.soufun.app:id/et_normal_login","18201147054")
        # self.commonTools.sendKeys("com.soufun.app:id/et_normal_login_pwd","HP19900114")
        # self.commonTools.clickElement("com.soufun.app:id/btn_normallogin_login")
        # self.commonTools.waitForElement("esfagent1123244",1)  #d登录成功
        # self.commonTools.clickElement("com.soufun.app:id/rl_home")
        # 买新房
        time.sleep(3)
        self.commonTools.clickElement( "//android.widget.GridView[@resource-id=\"com.soufun.app:id/data_list_view_my_gridview\"]/android.widget.RelativeLayout[1]")
        self.commonTools.waitForElement("com.soufun.app:id/iv_ad", 10)
        self.commonTools.clickElement("com.soufun.app:id/rl_district_navigationbar")
        self.commonTools.clickElement("大兴")
        self.commonTools.clickElement("生物医药基地")
        self.commonTools.clickElement("确认")
        self.commonTools.waitForElement("com.soufun.app:id/iv_ad",15)
        self.commonTools.clickElement("//android.widget.ListView[@resource-id=\"com.soufun.app:id/lv_xp\"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
        while True:
            if self.commonTools.checkElementIsShown("//android.widget.TextView[@resource-id=\"com.soufun.app:id/tv_dp_edit\"]"):
                self.commonTools.clickElement("//android.widget.TextView[@resource-id=\"com.soufun.app:id/tv_dp_edit\"]")
                break
            else:
                x_start, y_start, x_end, y_end= self.commonTools.swipeLocationy("com.soufun.app:id/ll_fragment_xf_detail_top")
                self.commonTools.swipe(x_start, y_start, x_end, y_end,1000)
        time.sleep(3)
        for i in range(100):
            x_start, y_start, x_end, y_end = self.commonTools.swipeLocationy("//android.widget.RelativeLayout[@resource-id=\"com.soufun.app:id/rootview\"]")
            self.commonTools.swipe(x_start, y_start, x_end, y_end , 500)
        time.sleep(3)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_Logout)
    unittest.TextTestRunner(verbosity=2).run(suite)

