# -*- coding: utf-8 -*-

import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from runner.testrunner import Runer
from testcase.cases.day10_case1 import ApiCase as ApiCase1
from testcase.cases.day10_case2 import ApiCase as ApiCase2

t = Runer(u"测试用例-hup", u"接口测试", u"测试一")
suite = t.load_test_from_class((ApiCase1,ApiCase2))
t.run(suite)
