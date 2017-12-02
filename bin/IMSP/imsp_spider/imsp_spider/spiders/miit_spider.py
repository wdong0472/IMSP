# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
import sys   
from ..items import miit_item

reload(sys) 
sys.setdefaultencoding('utf-8') 

class MiitSpider(scrapy.Spider):
    name = "miit"
    allowed_domains = ["miit.gov.cn"]
    start_urls = [
     'http://www.miit.gov.cn/',
    ]
    
    def parse(self,response):

        docs = response.xpath('//div[@class="common_one"]//div[@class="szyw_con"]//a')
        for doc in docs:
            item = miit_item.MiitSpiderItem()
            item['title'] = doc.xpath('./text()').extract()[0]
            item['link'] = doc.xpath('./@href').extract()[0]
            yield item 

