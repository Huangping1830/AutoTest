#coding:utf-8
import xlrd
data = xlrd.open_workbook('../urldata/data.xlsx')
tables = data.sheets()[0]
print tables.nrows  #行数   拿到行数，确认接口数量
print tables.ncols  #列数
print tables.cell_value(2,3)  #从（0,0）开始计
print data.sheet_names()