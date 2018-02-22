# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class WorksSpider(CrawlSpider):
    name = 'works'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    pgone = LinkExtractor(r'start=\d+')

    rules = (
        Rule(pgone, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for x in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TencentItem()
            item['name'] = x.xpath('.//td[1]/a/text()').extract()[0].encode('utf-8')
            item['link'] = x.xpath('.//td[1]/a/@href').extract()[0].encode('utf-8')
            item['leibie'] = x.xpath('.//td[2]/text()').extract()[0].encode('utf-8')
            item['num'] = x.xpath('.//td[3]/text()').extract()[0].encode('utf-8')
            item['workplace'] = x.xpath('.//td[4]/text()').extract()[0].encode('utf-8')
            item['time'] = x.xpath('.//td[5]/text()').extract()[0].encode('utf-8')
            yield item
