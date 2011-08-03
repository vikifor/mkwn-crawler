#!/usr/bin/python -*- coding=utf-8 -*-
# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawler'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DEFAULT_ITEM_CLASS = 'crawler.items.TextDataItem'
USER_AGENT = '%s/%s' % ('MkWordnet scraper - Scrapy 0.12 (Македонска верзија на Princeton Wordnet)', BOT_VERSION)

HTTPCACHE_DIR = "cache"
HTTPCACHE_EXPIRATION_SECS = 3200
DOWNLOAD_DELAY = 0.25 # 250 ms of delay

ITEM_PIPELINES = [
    'crawler.pipelines.CrawlerPipeline',
]

DOWNLOAD_DELAY = 4

ENV = 'local'

DATA_SETTINGS = {
    'local':{
        'couchdb_server':'http://localhost:5984/mkwordnet_db',
     },
    'remote':{
        'couchdb_server':'http://mkwordnet.hopto.org:5984/mkwordnet_db',
     }
}
# LOG_LEVEL='INFO'

