# -*- coding: utf-8 -*-

import time
import unittest
from unittest.suite import TestSuite
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from runner.HTMLTestRunnerEN import HTMLTestRunner
from path_dir import *


class Runer(object):

    def __init__(self, title="Interface Automation", desc="Interface Automation Results", run_envi="Test Envionment"):
        """测试报告参数信息
        Args:
            title(str): 日志标题
            desc(str): 日志结果
            run_envi(str): 运行环境
        """
        self.title = title
        self.desc = desc
        self.run_envi = run_envi


    def _get_report_name(self):
        """获取测试报告文件名称，包含路径"""
        report_name = report_dir + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        if os.path.exists(report_name + ".html"):
            i = 1
            temp_name = "".join([report_name, "_", str(i), ".html"])
            if not os.path.exists(report_name):
                return os.path.realpath(temp_name)
            else:
                i += 1
        else:
            return os.path.realpath(report_name+".html")

    def load_test_from_class(self, test_calsses):
        suite = TestSuite()
        for test_class in test_calsses:
            tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
            suite.addTest(tests)
        return suite

    def load_test_from_suite(self, test_modules):
        suite = TestSuite()
        for test_module in test_modules:
            tests = unittest.defaultTestLoader.loadTestsFromModule(test_module)
            suite.addTest(tests)
        return suite

    def load_test_from_names(self, test_names):
        suite = TestSuite()
        for test_name in test_names:
            tests = unittest.defaultTestLoader.loadTestsFromName(test_name)
            suite.addTest(tests)
        return suite

    def run(self, test_suite):
        """执行测试用例"""
        report_name = self._get_report_name()
        fp = open(report_name, "wb")
        runner = HTMLTestRunner(stream=fp, title=unicode(self.title), description=unicode(self.desc))
        runner.run(test_suite)
        fp.close()
        # os.system(report_name)

if __name__ == "__main__":
    a = Runer()
    print a._get_report_name()
    a.run()
