#coding:utf-8
import os

path_root = os.path.dirname(__file__)
# print(path_root)
path_config = os.path.join(path_root, "commonTools/configs.conf").replace("\\", "/")
log_dir = os.path.join(path_root, "log/").replace("\\", "/")
report_dir = os.path.join(path_root, "report/").replace("\\", "/")
excel_dir = os.path.join(path_root, "exceldata/").replace("\\", "/")
data_dir = os.path.join(path_root,"dataconfig/").replace("\\","/")







