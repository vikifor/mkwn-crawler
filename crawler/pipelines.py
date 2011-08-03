#!/usr/bin/python -*- coding=utf-8 -*-

import couchdb
import hashlib
import settings

class CrawlerPipeline(object):
    """Запишување на податоците во CouchDB"""
    def __init__(self):
        self.db = couchdb.Database(settings.DATA_SETTINGS[settings.ENV]['couchdb_server'])

    def process_item(self, item, spider):
        if item is None:
            return item
        # Креирање на python dictionary од внесените податоци (со мета податоците)
        d = dict(item)
        d['meta'] = dict(item.meta)
        # Генерирање на уникатед ID од URL-то
        d_id = hashlib.md5(d['meta']['url']).hexdigest()

        if d_id in self.db:
            doc = self.db.get(d_id)
            if len(doc['text']) > 0 and doc['text'].find(d['text']) != -1:
                # ако постои документ од авторот со ист наслов додади го новиот текстот на постоечкиот
                doc = self.db.get(d_id)
                doc['text'] = "%s\n%s" % (doc['text'], d['text'])
        else:
            doc = d

        self.db[d_id] = doc
        return item
