"""糗事百科Scrapy爬虫笔记"""
1.response是一个"scrapy.http.response.html.HtmlResponse"对象，
    可以执行"xpath"和"css"语法来提取数据
2.提取出来的数据，是一个"Selector"或者是一个"SelectorList"对象，
    如果想要获取其中的字符串。那么应该执行"getall"或者"get"方法
3.getall方法：获取"Selector"中的所有文本，返回的是一个列表
4.get方法：获取的是"Selector"中的第一个文本，返回的是str类型
5.如果数据解析回来，要传递给pipline处理。那么可以使用"yield"来返回。
    或者是收集所有的item到列表中，最后统一使用return返回
6.item: 建议在item.py中定义好模型。以后就不要使用字典
7.pipline：这个是专门用来保存数据的。其中三个方法是会经常使用的。
    * "open_spider(self, spider)": 当爬虫被打开的时候执行
    * "process_item(self, item, spider)": 当爬虫有item传递来的时候被调用
    * "close_spider(self, spider)": 当爬虫关闭的时候会被调用
    要激活pipline，应该在"settings.py"中设置"ITEM_PIPLINES"。
8.在piplines.py中保存数据可用JsonItemExporter，JsonLinesItemExporter
    在保存数据时，可以使用这两个类，让操作更简单
    "JsonItemExporter": 优势：储存的数据是一个满足json规则的数据，
                        劣势：数据量比较大后，会很耗占用内存
    "JsonLinesItemExporter": 优势：数据实时存储，不占内存，比较安全
                             劣势：每一个字典是一行，不是一个满足json的格式文件