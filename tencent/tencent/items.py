# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    leibie = scrapy.Field()
    num = scrapy.Field()
    workplace = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
