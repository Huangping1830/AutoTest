#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from testcase.databasecase import BaseCase





class HttpbinTestCase(BaseCase):


    def setUp(cls):
        super(HttpbinTestCase, cls).setUp()
        cls.sheet = "apidata"


    def tearDown(cls):
        super(HttpbinTestCase, cls).tearDown()
        cls.w.save(cls.nowTimeName)


    def test_get_method(self):
        res = self.sender(api_name="get_method")
        self.logger.info(''.join([self.log_cur_name(), " - response : ", str(res)]))

    def test_post_method(self):
        res =self.sender(api_name="post_method")
        self.logger.info(''.join([self.log_cur_name(), " - response : ", str(res)]))

if __name__ == "__main__":
    unittest.main()
