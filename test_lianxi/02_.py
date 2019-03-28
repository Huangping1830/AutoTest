#coding=utf-8
#  __author__ = 'zhengtong'


class Person:
    """
    不带object
    """
    name="zhengtong"

class Animal(object):
    """
    带有object
  """
    name="chonghong"

if __name__=="__main__":
    x=Person()
    print "Person",dir(x)
    y=Animal()
    print "Animal",dir(y)