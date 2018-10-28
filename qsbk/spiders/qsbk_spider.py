# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse   # response的对象，可以查看有什么方法
from scrapy.selector.unified import SelectorList


class QsbkSpiderSpider(scrapy.Spider):
    # 名字必须是唯一的
    name = 'qsbk_spider'
    # 允许的域名，限制爬虫的范围
    allowed_domains = ['qiushibaike.com']
    # 开始的url，可传递多个
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        # 返回结果为SelectorList
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        items = []
        for duanzidiv in duanzidivs:
            # 循环每一个Selector,调用get()返回unicode字符串
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            # 获取所有内容getall,返回一个列表
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            # "".join把列表转换为字符串
            content = "".join(content).strip()
            # 约束我们传递的参数数量
            item = QsbkItem(author=author, content=content)
            # 第一种方式：转换为生成器
            yield item
            # 第二种方式定义列表，return列表
        #     items.append(item)
        # return items
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            # 携带当前参数(下一页的url)，回调当前请求并再次解析
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)

