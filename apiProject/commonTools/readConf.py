import ConfigParser
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

if __name__ == "__main__":
    conf = myconf()
    conf.read("configs.conf")
    print conf.sections()
    for  i in conf.sections():
        print conf.options(i)
        for option in  conf.options(i):
            print option,conf.get(i,option)