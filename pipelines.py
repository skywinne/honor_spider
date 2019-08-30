# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

from .items import HonorItem


# 测试将数据存为
class HonorPipeline(object):
    def open_spider(self, spider):
        self.f = open("honor.json", "w")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item)) + ',\n'
        self.f.write(json_str)

    def close_spider(self, spider):
        self.f.close()

