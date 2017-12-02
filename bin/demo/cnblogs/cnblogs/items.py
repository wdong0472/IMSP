# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StackItem(scrapy.Item):
    # define the fields for your item here like:
    title=scrapy.Field()
    url=scrapy.Field()

class TuchongItem(scrapy.Item):
    post_id = scrapy.Field()
    site_id = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    image_count = scrapy.Field()
    images = scrapy.Field()
    tags = scrapy.Field()
    excerpt = scrapy.Field()    
