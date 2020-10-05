import scrapy
import re
from datetime import datetime
import time
import pandas as pd
from globocrawl.items import GlobocrawlItem
from globocrawl.middlewares import GlobocrawlSpiderMiddleware

class ContentcrawlSpider(scrapy.Spider):
    name = 'content2019'
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

        date = response.css('p>time::text').extract()
        main = response.css("h1.content-head__title::text").getall()
        sub = response.css("h2.content-head__subtitle::text").getall()
        content = ''.join(response.css("p.content-text__container::text").getall()).replace("\n","").strip()
        print("*"*50)
        item['date'] = date
        item['main_title'] = main
        item['sub_title'] = sub
        item['content'] = content

        yield item
      
            
