# -*- coding: utf-8 -*-

import json
from excel import ExcelHelper


def get_excel_case_list(excel_name, sheet_name, api_name):
    """获取excel中指定接口名称的用例列表
    Args:
        excel_name: excel文件名称
        sheet_name: 工作簿名称
        api_name: 接口名称
    """
    return ExcelHelper(excel_name, sheet_name).get_case_list(api_name)


def get_api_names(excel_name, sheet_name):
    """获取excel中接口名称列表，去重处理"""
    return ExcelHelper(excel_name,sheet_name).get_all_api_names()


def get_all_api_names(excel_name, sheet_name):
    """获取excel中接口名称列表, 未做去重处理 """
    return ExcelHelper(excel_name, sheet_name).get_all_api_names()


def get_app_api_name_docs(excel_name, sheet_name):
    """获取excel中接口说明信息 """
    return ExcelHelper(excel_name, sheet_name).get_all_api_name_docs()


def get_excel_value(excel_name, sheet_name, row_name, col_name):
    """获取excel数据文件中单元格的值"""
    return ExcelHelper(excel_name, sheet_name).get_value(row_name, col_name)


def compare_json_object(except_json, fact_json):
    """json对象比较，先比较code值和msg信息，然后比较data中的key字段
    Args:
        except_json: 期望返回的json对象
        fact_json: 实际返回的json对象
     """
    flag = True
    ex_dic = json.loads(except_json)
    fact_dic = json.loads(fact_json)
    try:
        if ex_dic["code"] == fact_dic["code"]:
            if ex_dic["msg"] != fact_dic["msg"]:
                print "msg不同"
                flag = False
                return flag
        else:
            print "".join(["code值不同, 实际返回code值为：", str(fact_dic["code"]),
                           ", 预期返回code值为：", str(ex_dic["code"])])
            flag = False
            return flag
        for key in ex_dic:
            if key not in fact_dic:
                print "没有这个{0}字段".format(key)
                flag = False
            if isinstance(ex_dic[key], dict):
                son_dic = ex_dic[key]
                for son_key in son_dic.keys():
                    if son_key not in fact_dic[key]:
                        print "没有这个%s字段".format(son_key)
                        flag = False
    except KeyError:
        if cmp(ex_dic, fact_dic) != 0:
            flag = False

    return flag

