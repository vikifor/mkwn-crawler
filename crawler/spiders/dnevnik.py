#!/usr/bin/python -*- coding=utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,  Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, MapCompose
from crawler.items import TextDataItem


class DnevnikLoader(XPathItemLoader):
    default_input_processor = MapCompose(unicode)
    default_output_processor = TakeFirst()
    dns_out = Compose(lambda v: zip(v[::2],  v[1::2]))


class DnevnikSpider(CrawlSpider):
    name = "dnevnik.com.mk"
    allowed_domains = ["dnevnik.com.mk"] #, "star.dnevnik.com.mk"]
    start_urls = [
        "http://dnevnik.com.mk"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'http://dnevnik.com.mk/default\.asp\?ItemID=.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = TextDataItem()

        item['name'] = hxs.select('//*[@id="ArticleTitle"]/text()').extract()
        if item['name'] is None or len(item['name']) == 0:
            return None
        item['text'] = hxs.select('//*[@id="ArticleText"]//text()').extract()
        item['kind'] = hxs.select('//*[@id="ArticleHeading"]/text()').extract()
        item.meta['author'] = hxs.select('/html/body/div[2]/div[2]/table/tbody/tr/td[3]/table[4]/tbody/tr/td/table/tbody/tr/td[3]/div[11]/table/tbody/tr/td/p[5]/text()').extract()
        item.meta['style'] = 'vesti'
        item.meta['url'] = response.url
        return item
