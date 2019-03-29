#coding:utf-8
import json
'''
重构json工具类
'''
class OperationJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/cookie.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #防止文件打开后，忘记关闭，with..as 会自动关闭文件！！！
        with open("../dataconfig/login.json") as fp:
            data = json.load(fp)   #加载json文件
            return data

    #根据关键字获取数据
    def get_data(self,id):
        key = str(id)
        #print self.data[key]
        return self.data[key]

if __name__ =='__main__':
    opjson = OperationJson()
    print(opjson.get_data('getdata1'))




