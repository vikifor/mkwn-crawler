#!/bin/python -*- coding=utf-8 -*-

import couchdb
import hashlib
from . import settings

class CrawlerPipeline(object):
    """Запишување на податоците во CouchDB"""
    def __init__(self):
        self.db = couchdb.Database(settings.DATA_SETTINGS[settings.ENV]['couchdb_server'])

    def process_item(self,  domain,  item):
        # Креирање на python dictionary од внесените податоци (со мета податоците)
        d = dict(item)
        d['meta'] = dict(item.meta)
        # Генерирање на уникатед ID од насловот и авторот
        d_id = hashlib.md5("%s%s" % (item['name'], item.meta.get('author', 'mkwordnet'))).hexdigest()
        if d_id in self.db and self.db[d_id]['text'].find(item['text']) != -1:
            # ако постои документ од авторот со ист наслов додади го новиот текстот на постоечкиот
            doc = self.db[d_id]
            doc['text'] = "%s\n%s" % (doc['text'], d['text'])
            d = doc
        self.db[d_id] = d
        return item
