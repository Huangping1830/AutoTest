#coding:utf-8
import requests

class OperatinHeader:
    def __init__(self):
        pass

    def get_header(self):
        pass


if __name__ == '__main__':
    url =""
    data = {"username":
            "password":
            }
    res = requests.post(url,data).json()
    response_url = res['data']['url'][0]
    requests_url = response_url + "&callback=jQuery2100824..."
    cookie = requests.get(requests_url).cookies
    requests.utils.dict_from_cookiejar(cookie)
    print cookie['apsid']

