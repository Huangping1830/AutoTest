# coding: utf-8
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
        self.commonTools.waitForElement("我的",3)
        self.commonTools.clickElement("我的")
        time.sleep(3)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_Logout)
    unittest.TextTestRunner(verbosity=2).run(suite)