#coding:utf-8
'''
get,post封装
'''
import requests
import json

class RunMethod:
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header)
        else:
            res = requests.get(url=url,params=data)
        #print res.status_code
        return res

    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            #print "无header"
        #print res.status_code
        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header).json()
        if method == 'get':
            res = self.get_main(url,data,header).json()
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        #request_res = json.dumps(res.json())
        #return

if __name__ == '__main__':
    run = RunMethod()
    url = "http://web-api-test.energymost.com/api/vee/getdatastructure"
    data = {
        "UserId": 312135,
        "CustomerId": 347373
    }
    res = run.run_main('post',url,data)
    print(res)
