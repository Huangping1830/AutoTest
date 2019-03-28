# -*- coding: utf-8 -*-
import os
import sys
import unittest
import logging
from appProject.util.pathTools import log_path,conf_path
from appProject.util.commonTools import CommonTools

class BaseCase(unittest.TestCase):
    """测试用例基础类,"""

    @classmethod
    def setUpClass(cls):
        """执行用例开始时初始化,这里面应该有初始化， 
        比如logger， 比如db，这样你继承它的case， 
        都可以在自己的setUp里执行base的setUp
        """
        res_log_path = os.path.join(log_path, '{}.log'.format(cls.__name__))
        cls.logger = cls.add_logger(log_name=cls.__name__, log_file_path=res_log_path,
                                    log_level=logging.INFO)
        conf_path_name = conf_path + "configs.conf"
        cls.commonTools = CommonTools(conf_path_name)
        cls.commonTools.initDriver()
        cls.dict1 = {}

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
    def tearDown(self):
        """执行用例结束时初始化"""
        pass






