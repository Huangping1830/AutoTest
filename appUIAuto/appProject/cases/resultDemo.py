#-*-coding:utf-8-*-
from __future__ import absolute_import

import time
import unittest

from appProject.util.commonTools import CommonTools
from appProject.util.resultTools import createReport


class Login_Logout(unittest.TestCase):
    def setUp(self):
        self.commonTools = CommonTools("configs.conf")
        self.commonTools.initDriver()


    def tearDown(self):
        self.commonTools.quitDriver()


    def test_run(self):
        time.sleep(3)
        self.commonTools.waitForElement("我的", 3)
        self.commonTools.clickElement("我的")
        time.sleep(3)
        self.assertEqual(2, 2)



def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Login_Logout("test_run"))
    return suiteTest
if __name__ == "__main__":
    createReport(Suite(),u"开源中国测试测试用例",u"开源中国登陆测试用例")
    # filename = "C:\\Users\\YK-DZ-34416\\Desktop\\appiumDemo\\appProject\\resultReport\\1.html"
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'那个人粉嫩', description=u'反反复复')
    # runner.run(Suite())
    # fp.close()




