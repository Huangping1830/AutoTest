# -*- coding: utf-8 -*-

import sys
import unittest
import logging
import datetime
from path_dir import *
from commonTools.apiTools import ApiTools
from cfg.excel import ExcelHelper
class BaseCase(unittest.TestCase):
    """测试用例基础类,"""

    @classmethod
    def setUpClass(cls):
        """执行用例开始时初始化,这里面应该有初始化， 
        比如logger， 比如db，这样你继承它的case， 
        都可以在自己的setUp里执行base的setUp
        """
        log_path = os.path.join(log_dir, '{}.log'.format(cls.__name__))
        cls.logger = cls.add_logger(log_name=cls.__name__, log_file_path=log_path,
                                    log_level=logging.INFO)
        cls.apitool = ApiTools()
        cls.dict1 = {}
        cls.excelhelper = ExcelHelper("apidata.xlsx", "apidata")
        cls.file_path_name = cls.excelhelper.file_path_name
        cls.nowTime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        cls.nowTimeName = cls.file_path_name + "_report" + str(cls.nowTime) + ".xlsx"
    @staticmethod
    def add_logger(log_name, log_file_path, log_level):
        # 创建一个logging
        logger = logging.getLogger(log_name)
        logger.setLevel(log_level)
        # 创建一个hander，用于写入日志文件
        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        return logger
    def log_cur_name(self):
        return str(sys._getframe().f_back.f_code.co_name)

    def sender(self, api_name=None):

        fact_resp = self.send(api_name)
        expe_resp = self.excelhelper.get_value(api_name, "expect")
        result = self.excelhelper.compare_json_object(expe_resp, fact_resp)
        self.w = self.excelhelper.write_report(api_name, fact_resp,result)
        return fact_resp,expe_resp
    def sendercase(self, api_name=None,data=None):

        fact_resp = self.sendcase(api_name,data)
        expe_resp = self.excelhelper.get_value(api_name, "expect")
        result = self.excelhelper.compare_json_object(expe_resp, fact_resp)
        self.w = self.excelhelper.write_report(api_name, fact_resp,result)
        return fact_resp,expe_resp


    def send(self, api_name=None):
        """发送请求
        Args:
            data: 接口请求参数
        Returns:
            response: 接口响应信息 
        """
        import requests
        url = self.excelhelper.get_value(api_name, "url")
        path = self.excelhelper.get_value(api_name, "request_path")
        method = self.excelhelper.get_value(api_name, "request_meth")
        data = self.excelhelper.get_value(api_name, "request_para")
        header = self.excelhelper.get_value(api_name, "request_header")
        print url, path, method, data, header
        if method == "get":
            r = requests.get(headers=eval(header),url=url+path, params=data)
            print r.text
        elif method == "post":
            r = requests.post(headers=eval(header),url=url+path, data=data)
            print r.text

        else:
            raise
        if r.status_code != 200:
            self.logger.info(''.join([api_name, " - response staus_code : ", r.status_code]))
        response = r.json()
        return response
    def sendcase(self, api_name=None,data=None):
        """发送请求
        Args:
            data: 接口请求参数
        Returns:
            response: 接口响应信息
        """
        import requests
        url = self.excelhelper.get_value(api_name, "url")
        path = self.excelhelper.get_value(api_name, "request_path")
        method = self.excelhelper.get_value(api_name, "request_meth")
        header = self.excelhelper.get_value(api_name, "request_header")
        print url, path, method, data, header
        if method == "get":
            r = requests.get(headers=eval(header),url=url+path, params=data)
            print r.text
        elif method == "post":
            r = requests.post(headers=eval(header),url=url+path, data=data)
            print r.text

        else:
            raise
        if r.status_code != 200:
            self.logger.info(''.join([api_name, " - response staus_code : ", r.status_code]))
        response = r.json()
        return response
    @classmethod
    def tearDownClass(cls):
        """执行用例结束时初始化"""
        pass







