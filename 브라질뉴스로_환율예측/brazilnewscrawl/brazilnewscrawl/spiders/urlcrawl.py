import re, requests, json, urllib, datetime, scrapy, time
import pandas as pd
from globocrawl.items import GlobocrawlItem
from globocrawl.middlewares import GlobocrawlSpiderMiddleware


class UrlcrawlSpider(scrapy.Spider):
    name = 'urlcrawl'
    # allowed_domains = ['google.com']
    # start_urls = ['http://google.com/']

    def __init__(self,file):
        first_url = 'https://www.google.com/search?q=economia+site:https://g1.globo.com/economia/noticia/2011/0{}&lr=&newwindow=1&hl=ko&tbm=nws&ei=htJ0X8v2HNfrwQPypbaIDA&start={}0&sa=N&ved=0ahUKEwjL0fGKxZHsAhXXdXAKHfKSDcE48AEQ8tMDCIkB&biw=1012&bih=838&dpr=1.13'
        self.urls = []
        for i in range(1,13):
            if i < 10:
                a = str(i).rjust(2,'0')
            else:
                a = i
            
            for j in range(30):
    
                self.urls.append(first_url.format(a,j))

    def start_requests(self) :
        for url in self.urls :
            yield scrapy.Request(url=url)


    def parse(self, response):
        #print(response.text)
        result_dic = json.loads(response.text)
        item = InstacrawlItem()
        # self.crawling_count  += 1
        # if self.crawling_count % 200 == 0:
        #     time.sleep(700)

        #print("*"*50)
        #print(result_dic['graphql']['user']['username'])
        #print(result_dic['graphql']['user']['biography'])
        item['articleurl'] = result_dic['data']['user']['reel']['id']
        yield item