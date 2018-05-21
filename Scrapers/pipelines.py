# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bson import json_util
import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('sarees.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), default=json_util.default) + "\n"
        self.file.write(line)
        return item
