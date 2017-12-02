# -*- coding: utf-8 -*-
import sys
from suds.client import Client

reload(sys) 
sys.setdefaultencoding('utf-8') 

def websevice():
    """
    创建websevice请求
"""
    url = settings.WebSeviceUrl
    client = Client(url)
    result = client.service
    return result


#创建websev 
websev = websevice()

#调用方式websev.方法名（参数）
ws = websev.getRealInfo(param)
