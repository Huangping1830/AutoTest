# -*- coding: utf-8 -*-
from __future__ import absolute_import

import time
import unittest

from appProject.util.commonTools import CommonTools
from appProject.util.pic import picName


class Login_Logout(unittest.TestCase):
    def setUp(self):
        self.commonTools =CommonTools("configs.conf")
        self.commonTools.initDriver()
    def tearDown(self):
        self.commonTools.quitDriver()
    def test_run(self):
        time.sleep(5)
        self.commonTools.findElement("android:id/button2")
        self.commonTools.clickElement("android:id/button2")
        tuple = self.commonTools.swipeLocation("net.oschina.app:id/ll_title")
        self.commonTools.swipe(tuple[0],tuple[1],tuple[2],tuple[3],500)
        time.sleep(2)
        # 保存截图
        self.commonTools.saveScreenshot(picName(self))
        time.sleep(3)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_Logout)
    unittest.TextTestRunner(verbosity=2).run(suite)