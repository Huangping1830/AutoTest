
import sys
def logs():
    print sys._getframe().f_code.co_name
    print sys._getframe().f_back.f_code.co_name
def get_cur_info() :
    logs()
get_cur_info()