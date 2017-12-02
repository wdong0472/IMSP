# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from myblog.models import ArtiInfo 

def index(request): 
    article = ArtiInfo.objects[:10] #只显示前10个内容 
    context = { 
        'ArtiInfo':article 
    } 

    return render(request, 'index.html', context) # 传递context参数
