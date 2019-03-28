# -*- coding: utf-8 -*-
from __future__ import absolute_import

import time
import unittest

from appProject.util.commonTools import CommonTools


class Login_Logout(unittest.TestCase):
    def setUp(self):
        self.commonTools =CommonTools("configs.conf")
        self.commonTools.initDriver()
    def tearDown(self):
        self.commonTools.quitDriver()
    def test_run(self):
        time.sleep(3)
        self.commonTools.clickElement("android:id/button2")
        self.commonTools.clickElement("我的")
        time.sleep(2)
        # 点击设置
        self.commonTools.clickElement("net.oschina.app:id/iv_logo_setting")
        # 判断注销按钮是否存在，存在点击注销
        exit = self.commonTools.checkElementIsShown("net.oschina.app:id/rl_cancel")
        if exit == True :
            self.commonTools.clickElement("net.oschina.app:id/rl_cancel")
            self.commonTools.clickElement("android.widget.ImageButton")
        else:
            self.commonTools.clickElement("android.widget.ImageButton")
        # 点击头像
        self.commonTools.clickElement("net.oschina.app:id/iv_portrait")

        self.commonTools.clickElement("net.oschina.app:id/et_login_username")
        self.commonTools.clearTextEdit("net.oschina.app:id/et_login_username")
        self.commonTools.sendKeys("net.oschina.app:id/et_login_username","xzt875@126.com")

        self.commonTools.clickElement("net.oschina.app:id/et_login_pwd")
        self.commonTools.sendKeys("net.oschina.app:id/et_login_pwd","13419926370qaz")
        self.commonTools.clickElement("net.oschina.app:id/bt_login_submit")

        time.sleep(3)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_Logout)
    unittest.TextTestRunner(verbosity=2).run(suite)