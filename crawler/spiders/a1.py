#!/usr/bin/python -*- coding=utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,  Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, MapCompose
from crawler.items import TextDataItem


class A1Spider(CrawlSpider):
    name = "a1"
    allowed_domains = ["a1.com.mk"]
    start_urls = [
        "http://a1.com.mk"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/vesti/kategorija\.aspx\?KatID=\d+'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'/vesti/fudbal/liga\.asp?ID=\d+'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'/vesti/default.aspx\?VestID=\d+'), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=r'/vesti/sport.asp\?VestID=\d+'), callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = TextDataItem()

        item['name'] = "".join(hxs.select('//*[@id="H2naslov"]/text()').extract())
        tt = hxs.select('/html/body/form/table[3]')
        item['text'] = "\n".join(tt.select('.//p//text()').extract())
        item['kind'] = 'vest'
        item.meta['author'] = 'a1.com.mk'
        item.meta['style'] = 'vesti'
        item.meta['url'] = response.url
        return item




class A1NovinariSpider(A1Spider):
    """
    Скоро ист како a1.com.mk само што почнува од листа на новинари
    и ги следи сите страни со статии групирани по новинар.
    Многу почист начин на за земање на сите содржини кои ги нуди сајтот.
    """
    name = "a1-novinari"
    start_urls = [
        "http://a1.com.mk/vesti/arhiva-novinari.asp"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/vesti/arhiva-novinar.asp\?ID=\d+&Strana=\d+'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'/vesti/\w+.asp?\?VestID=\d+'), callback='parse_item'),
    )
