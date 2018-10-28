from scrapy import cmdline

# 设置运行spider的简单方式
# 第一种
# cmdline.execute("scrapy crawl qsbk_spider".split())
# 第二种
cmdline.execute(["scrapy", "crawl", "qsbk_spider"])