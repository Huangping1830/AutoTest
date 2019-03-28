#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from testcase.databasecase import BaseCase


class Juejin(BaseCase):
    def setUp(cls):
        super(Juejin, cls).setUp()
        cls.sheet = "apidata"


    def tearDown(cls):
        super(Juejin, cls).tearDown()
        cls.w.save(cls.nowTimeName)

    def test_alogin(self):
        res = self.sender(api_name="juejin_login")
        self.dict1["token"] = res[0]["d"]["token"]
        self.dict1["user_id"] = res[0]["d"]["user_id"]
        self.logger.info(''.join([self.log_cur_name(), " - response : ", str(res)]))
    def test_bgetUserInfo(self):
        datastr="uid=%s&current_uid=%s&token=%s&device_id=de00b0cf-25be-4036-beb4-b8b3d19e190e&src=android" %(self.dict1["user_id"],self.dict1["user_id"],self.dict1["token"])
        res = self.sendercase(api_name="juejin_getUserInfo",data=datastr)
        self.logger.info(''.join([self.log_cur_name(), " - response : ", str(res)]))




if __name__ == "__main__":
    unittest.main()
