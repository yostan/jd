# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from datetime import date, datetime
from collections import OrderedDict


class JdPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('jd_comments_utf8_01.json', 'w', encoding='utf-8')  # append

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        # self.file.flush()
        return item

    def spider_closed(self, spider):
        self.file.close()

