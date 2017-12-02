# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
import sys   

reload(sys) 
sys.setdefaultencoding('utf-8') 

class MiitSpider(scrapy.Spider):
    name = "miit"
    allowed_domains = ["www.miit.gov.cn"]
    start_urls = [
     'http://www.miit.gov.cn/',
    ]

    def parse(self, response):
        title = response.xpath('//div[@class="common_one"]//div[@class="szyw_con"]//a/text()').extract()
        link = response.xpath('//div[@class="common_one"]//div[@class="szyw_con"]//a/@href').extract()
        print(title)
        print(link)

