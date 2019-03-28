#-*-coding:utf-8-*-
import os
import time
import HTMLTestRunner

from pathTools import screenShot_path,resultReport_path


def createName(fileType):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    if fileType == "image":
        res_name = screenShot_path + now + ".png"
        return res_name
    elif fileType == "html":
        res_name = resultReport_path +now+"result.html"
        return res_name
    else:
        print "type error"


def createReport(sutie,title,desc):
    res_name = createName("html")
    fb = open(res_name,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=title, description=desc)
    runner.run(sutie)
    fb.close()
