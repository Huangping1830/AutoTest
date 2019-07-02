# coding:utf-8
import xlrd
from xlutils.copy import copy
from path_dir import *
'''
重构操作Excel函数
'''
class WriteExcel:
    def __init__(self,file_name=None,sheet_id=0):
        if file_name:
            self.file_name = data_dir + file_name
        else:
            self.file_name =data_dir + "Interfacedata.xls"
        self.sheet_id = sheet_id

    #写入数据
    def write_value(self,row,id,order_id=None,order_time=None,person_num=None,person_list=None):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,0,id)
        sheet_data.write(row, 1, order_id)
        sheet_data.write(row, 2, order_time)
        sheet_data.write(row, 3, person_num)
        sheet_data.write(row, 4, person_list)
        write_data.save(self.file_name)

if __name__ == "__main__":
    opers = WriteExcel('data.xls')
    opers.write_value(5,121222222)


