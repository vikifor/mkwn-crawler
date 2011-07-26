#!/bin/python -*- coding=utf-8 -*-

# Ќе се креираат 2 Item објекти за секој најден текст:
# 1 - Главниот TextDataItem објект во кој ќе се чува текстот и податоците релевантни за проектот
# 2 - Metadata објект во кој се чуваат пропратните податоци кои не влијаат директно врз проектот

from scrapy.item import Item, Field

class Metadata(Item):
    author = Field()
    style = Field()

class TextDataItem(Item):
    kind = Field()
    name = Field()
    corpus = Field()
    text = Field()
    meta = Metadata()
