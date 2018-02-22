# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class TencentPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['名字','类别','人数','工作地点','发布时间','链接'])

    def process_item(self, item, spider):
        line = [item['name'],item['leibie'],item['num'],item['workplace'],item['time'],item['link']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('/home/python/tencent/works.xlsx')
