#!encoding=utf-8

import requests
import sys
sys.path.append("F:/05-workspace/AutoTest/apiProject")
from commonTools.readConf import myconf
from path_dir import *
import requests


class ApiTools(object):

    def __init__(self):
        self.readConf = myconf()
        self.readConf.read(path_config)
        self.apiCaps = dict(self.readConf.items("apiConfig"))
        self.headersCaps = dict(self.readConf.items("headersConfig"))
        self.req = requests.Session()
        if self.apiCaps["scheme"] == "https":
            self.apiCaps["verify"] = False
        else:
            self.apiCaps["verify"] = True


    def post_method(self, api, data):
        url = "%s://%s%s" % (self.apiCaps["scheme"], self.apiCaps["host"], api)
        res = self.req.post(url, headers=self.headersCaps, data=data, verify=self.apiCaps["verify"])
        return res

    def get_method(self, api, data):
        url = "%s://%s%s" % (self.apiCaps["scheme"], self.apiCaps["host"], api)
        res = self.req.get(url, headers=self.headersCaps, params=data,verify=self.apiCaps["verify"])
        return res

    def check_error(self, data):
        try:
            if data["code"] == 0:
                return data
            else:
                return data
        except Exception, e:
            return e


if __name__ == "__main__":
    t = ApiTools()
    r = t.post_method(api="/api/vee/getdatastructure",data="UserId=312135&CustomerId=347373")
    print r.status_code
    print r.json()
    #t.check_error(r)

