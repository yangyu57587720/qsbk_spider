# -*- coding: utf-8 -*-
"""保存数据的三种方式"""
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import json
# class QsbkPipeline(object):
#
#     def __init__(self):
#         # 打开文件句柄
#         self.fp = open("duanzi.json", "a+", encoding="utf-8")
#
#     def open_spider(self, spider):
#         print("爬虫开始了....")
#
#     def process_item(self, item, spider):
#         # 接受yield传参,序列化为json格式,不使用默认ascii码
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + "\n")
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束了.....")

# from scrapy.exporters import JsonItemExporter     # 先存内存，再一次写入
# # 引入json格式的导出器
# class QsbkPipeline(object):
#
#     def __init__(self):
#         # 打开文件句柄
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print("爬虫开始了....")
#
#     def process_item(self, item, spider):
#         # 接受yield传参,序列化为json格式,不使用默认ascii码
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         # 完成导入
#         self.fp.close()
#         print("爬虫结束了.....")

# 常用
from scrapy.exporters import JsonLinesItemExporter
# 引入json格式的导出器
class QsbkPipeline(object):

    def __init__(self):
        # 打开文件句柄
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")

    def open_spider(self, spider):
        print("爬虫开始了....")

    def process_item(self, item, spider):
        # 接受yield传参,序列化为json格式,不使用默认ascii码
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了.....")