# coding: utf-8
import unittest
import sys
sys.path.append('F:/05-workspare/AutoTest/appUIAuto')
from appProject.cases import case1
from appProject.util import resultTools

testunit = unittest.TestSuite()


# testunit.addTest(unittest.makeSuite(login.Login_Logout))
testunit.addTest(unittest.makeSuite(case1.LoginCase))


resultTools.createReport(testunit, title=u"开源中国测试报告", desc=u"开源中国测试报告")
