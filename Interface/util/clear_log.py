#coding:utf-8
'''
功能：清理日志文件，把三天前的日志删掉，保留今天、昨天和前天
'''
import os
import time
from path_dir import *

def Clear_log(N):
    file_list = get_all_file()
    for file in file_list:
        if file.endswith('.log'):
            f = os.path.split(file)[1]
            t = f[-14:-4]   #log名称
            if time.time()-StrToTimestamp(t) >= 24*60*60*int(N):
                os.remove(file)

def get_all_file(path = log_dir):
    file_list = []
    for cur_path,cur_dirs,cur_files in os.walk(path):
        for name in cur_files:
            file_list.append(os.path.join(cur_path,name))
    return file_list

def StrToTimestamp(Str=None,format='%Y-%m-%d'):
    if Str:
        timep = time.strptime(Str,format)
        res = time.mktime(timep)
    else:
        res=time.time()
    return int(res)


def read_account(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        res = f.readlines()
        print(res)
        f.seek(0)
        f.truncate()

# if "__name__" == "__main__":
a = get_all_file()
print(a)
# read_account(a)
# N = input("请输入需要清除几天前的日志：")
# Clear_log(N)