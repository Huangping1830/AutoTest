#conding:utf-8
from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)  #发布会标题
    limit = models.IntegerField()            #参加人数
    status = models.BooleanField()           #状态
    address = models.CharField(max_length=200) #地址
    start_time = models.DateTimeField('event time')  #发布会时间
    create_time = models.DateTimeField(auto_now=True) #创建时间（自动获取当前时间）

    def __str__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    #经过筛查，在创建多对一的关系的,需要在Foreign的第二参数中加入on_delete=models.CASCADE  主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    realname = models.CharField(max_length=64)     #
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

class Meta:
    unique_together = ("event","phone")

def _str_(self):
    return self.name