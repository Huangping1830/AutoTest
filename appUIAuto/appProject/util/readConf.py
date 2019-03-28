#!encoding=utf-8

import ConfigParser
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr
# conf = myconf()
# conf.read("configs.conf")
# print conf.sections()
# for  i in conf.sections():
#     print conf.options(i)
#     for option in  conf.options(i):
#         print option,conf.get(i,option)
#
# readConf = myconf()
# readConf.read("configs.conf")
# desired_caps = dict(readConf.items("deviceConfig"))
# print desired_caps


# conf = myconf()
# #用config对象读取配置文件
# conf.read("C:\\Users\\xcz\\Desktop\\RF0903codes\\day2\\appAuto\\appProject\\configs.conf")
# #以列表形式返回所有的section
# # sections = conf.sections()
# # res = conf.get('deviceConfig','platformName')
# # res = conf.options("deviceConfig")
# desired_caps = dict(conf.items("deviceConfig"))
# print desired_caps