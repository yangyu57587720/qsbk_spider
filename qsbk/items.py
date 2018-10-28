# -*- coding: utf-8 -*-
"""定义传递数据的模型"""
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QsbkItem(scrapy.Item):
    # 固定好需要传递什么参数
    author = scrapy.Field()
    content = scrapy.Field()
