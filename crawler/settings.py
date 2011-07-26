#!/bin/python -*- coding=utf-8 -*-
# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'MkWordnet scraper - Scrapy 0.10.4 (Македонска верзија на Princeton Wordnet)'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DEFAULT_ITEM_CLASS = 'crawler.items.TextDataItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

import os

ENV = 'local'

DATA_SETTINGS = {
    'local':{
        'couchdb_server':'http://localhost:5984/mkwordnet_db',
        'db':os.path.join(os.path.dirname(__file__), '../../test.db'),
     },
    'remote':{
        'couchdb_server':'http://mkwordnet.hopto.org:5984/mkwordnet_db',
     }
}
