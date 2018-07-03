# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MongoPipeline(object):

    collection_name = 'products'

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('host', 'localhost'),
            user=crawler.settings.get('username', 'admin'),
            password=crawler.settings.get('password', '12345'),
            database=crawler.settings.get('database', 'locator')
        )

    def open_spider(self, spider):
        self.client = MySQLdb.connect(self.host, self.user, self.password, self.database)
        self.db = self.client.cursor()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # self.db.execute("insert into product(name, description, category, price, price_old, storeUrl, images) values({name}, {description}, {category}, {price}, {price_old}, {storeUrl}, {images})".format(name=item["name"], description=item["description"], category=item["category"], price=item["price"], price_old=item["price_old"], storeUrl=item["storeUrl"], images=item["images"]))
        return item