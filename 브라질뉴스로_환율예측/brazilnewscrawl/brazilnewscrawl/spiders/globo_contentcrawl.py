import scrapy
import re
from datetime import datetime
import time
import pandas as pd
from globocrawl.items import GlobocrawlItem
from globocrawl.middlewares import GlobocrawlSpiderMiddleware

class ContentcrawlSpider(scrapy.Spider):
    name = 'contentcrawl'
    # allowed_domains = ['globo.com']
    # start_urls = ['http://globo.com/']
    crawling_count = 0

    def __init__(self, file):
        self.urls = list(pd.read_csv(file, header=None)[0])

    def start_requests(self) :
        for url in self.urls :
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = GlobocrawlItem()
        # self.crawling_count += 1
        # if self.crawling_count > 80:
        #     time.sleep(500)

        date = response.css('abbr.published').xpath("descendant-or-self::abbr[@class and contains(concat(' ', normalize-space(@class), ' '), ' published ')]/text()")[0].extract()
        main = response.css("div.materia-titulo h1::text").getall()
        sub = response.css("div.materia-titulo h2::text").getall()
        #main = response.css('div.materia-titulo').xpath("descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' materia-titulo ')]/descendant-or-self::*/h1")[0].extract()
        # sub = response.css('div.materia-titulo').xpath("descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' materia-titulo ')]/descendant-or-self::*/h2")[0].extract()
        content = ''.join(response.css("div#materia-letra p::text").getall()).replace("\n","").strip()
        print("*"*50)
        item['date'] = date
        item['main_title'] = main
        item['sub_title'] = sub
        item['content'] = content

        yield item
      
            
