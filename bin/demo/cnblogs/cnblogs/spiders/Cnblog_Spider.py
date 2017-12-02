# -*- coding: utf-8 -*-
import scrapy
import sys   

reload(sys) 
sys.setdefaultencoding('utf-8') 

class Cnblog_Spider(scrapy.Spider):

    name = "cnblog"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
     'https://www.cnblogs.com/',
    ]

    def parse(self, response):
        title = response.xpath('//a[@class="titlelnk"]/text()').extract()
        link = response.xpath('//a[@class="titlelnk"]/@href').extract()
        print(title)
        print(link)
