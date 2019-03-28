# -*- coding: utf-8 -*-

import os
import json
import xlrd
import datetime
from xlutils.copy import copy
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from path_dir import excel_dir
# 将配置内容进行缓存(读写内容很多只对读取做缓存)


class ExcelHelper(object):
    """读取excel数据文件工具类"""

    def __init__(self, file_name, sheet_name):
        """处理file_name为绝对路径
        Args:
            file_name(str): excel文件名称
            sheet_name(str): 存放数据文件的工作簿名称
        """

        self.file_path_name = unicode(excel_dir) + unicode(file_name)
        self.sheet_name = unicode(sheet_name)

        try:
            self.table = xlrd.open_workbook(self.file_path_name).sheet_by_name(self.sheet_name)
            self.write_table = xlrd.open_workbook(self.file_path_name)
            self.w = copy(self.write_table)
        except IOError, msg:
            print msg


    def get_value(self, row_name, col_name):
        """获取单元格的值
        Args：
            row_name(str): 单元格所在的行名称
            col_name(str): 单元格所在的列名称
        Returns：
            value(str): 返回单元格的值
        """
        rows = self.table.row_values(0)   # 获得第1行的数据列表，返回list
        print rows
        cols = self.table.col_values(0)   # 获得第1列的数据列表，返回list
        print cols
        row_index = cols.index(row_name)   #index：检查字符串中是否包括子字符串,返回字符串所在的行数
        print row_index

        col_index = rows.index(unicode(col_name))   #index：检查字符串中是否包括子字符串,返回字符串所在的列数
        value = self.table.cell(row_index, col_index).value
        return value

    def get_case_list(self, api_name):
        """获取用例列表，每个用例以字典形式返回
        Args：
            api_name(str): 接口名称
        Returns:
            case_list(list): 返回该接口的所有用例，返回数据类型为list 
         """

        row_index_list = self._get_row_index_list(api_name)
        case_list = self._get_cases_list(row_index_list)
        return case_list

    def _get_row_index_list(self, api_name):
        """获取接口名称的行索引列表
        Args:
            api_name(str): 接口名称
        Returns：
            row_index_list(list): 返回该接口名称所对应的列索引列表，返回格式list
        """
        col_names = self.table.col_values(0)   #列值
        row_index_list = []
        for col_index, col_name in enumerate(col_names):
            if col_name == api_name:
                row_index_list.append(col_index)
        return row_index_list

    def _get_cases_list(self, row_index_list):
        """获取接口用例集，每单个用例放到字典中，所有用例以列表形式返回
        Args：
            row_index_list(list): 接口行索引列表
         """
        cases_list = []
        for row_index in row_index_list:
            case_dic = {}
            rows = self.table.row_values(0)  #行值
            for row in rows:
                case_dic[row] = self.table.cell(row_index, self._get_col_index(row)).value
            cases_list.append(case_dic)
        return cases_list

    def _get_col_index(self, col_name):
        """根据列名称获取列索引值
        Args:
            col_name(str): 列名称
        Returns:
            col_index(int):列名称所在的索引值
         """
        rows = self.table.row_values(0)  #行值
        col_index = rows.index(col_name)  #获取所在行数
        return col_index

    def get_api_names(self):
        """获取excel中所有接口的接口名称，去重处理"""

        api_name_list = self.table.col_values(0)
        api_name_list.remove("api_name")
        new_list = []
        for api_name in api_name_list:
            if api_name not in new_list:
                new_list.append(api_name)
        return new_list

    def get_all_api_names(self):
        """获取excel中 所有接口的接口名称，不去重"""

        api_names_list = self.table.col_values(0)
        api_names_list.remove("api_name")
        return api_names_list

    def get_all_api_name_docs(self):
        """获取excel中所有的接口说明"""

        api_name_docs_list = self.table.col_values(2)
        api_name_docs_list.remove("case_doc")
        return api_name_docs_list

    def write_report(self,row_name,response,result):
        response_content = "response"
        result_content = "result"

        rows = self.table.row_values(0)
        cols = self.table.col_values(0)
        row_index = cols.index(unicode(row_name))
        response_col_index = rows.index(unicode(response_content))
        result_col_index = rows.index(unicode(result_content))
        list1 = []
        for sheet in xlrd.open_workbook(self.file_path_name).sheets():
            list1.append(sheet.name)
        res_index = list1.index(self.sheet_name)
        # w = copy(self.write_table)
        self.w.get_sheet(res_index).write(row_index, response_col_index, str(response))
        self.w.get_sheet(res_index).write(row_index, result_col_index, str(result))
        nowTime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        report_filename = self.file_path_name + "_report"+str(nowTime)+".xlsx"
        # w.save(report_filename)
        return self.w

    def compare_json_object(self, except_json, fact_json):
        """json对象比较，先比较code值和msg信息，然后比较data中的key字段
        Args:
            except_json: 期望返回的json对象
            fact_json: 实际返回的json对象
         """
        # import json
        # ex_dic=json.loads(except_json)
        ex_dic = eval(except_json)
        fact_dic = fact_json
        try:
            res = cmp(ex_dic, fact_dic)
            if res == 0:
                return "PASS"
            else:
                return "Fail"

        except Exception, e:
            return e
if __name__ == "__main__":
    a = ExcelHelper("apidata.xlsx", "apidata")
    # a.test1()
    # print a.getCaseList(u'登录')
    print a.get_value("juejin_login","response")


