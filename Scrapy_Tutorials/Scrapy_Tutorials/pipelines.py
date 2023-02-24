# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo


class MongodbPipeline:
    collection_name = 'transcripts'
    def open_spider(self, spider):
        logging.warning('Spider opened')
        self.client = pymongo.MongoClient("") #assigning and instance of MongoDB client
        self.db = self.client['Database_01214']#creating a database


    def close_spider(self, spider):
        logging.warning('Spider Closed')
        self.client.close()#closing the client after the execution is over

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
