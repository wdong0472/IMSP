# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mongoengine import * 

connect('test', host='127.0.0.1', port=27017) # 指明要连接的数据库 

class ArtiInfo(Document): 
    title = StringField() 
    url = StringField() 
    price = StringField() 
    pub_date = StringField() 
    look = StringField() 
    area = ListField(StringField()) # 定义列表类型 
    cates = ListField(StringField()) 

    meta = { 'collection': 'sample'} # 指明连接数据库的哪张表 

for i in ArtiInfo.objects[:10]: # 测试是否连接成功 
    print(i.title)
