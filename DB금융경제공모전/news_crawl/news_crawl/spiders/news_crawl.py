import scrapy
import re
from datetime import datetime
import pandas as pd
from news_crawl.items import NewsCrawlItem

class CrawlNewsSpider(scrapy.Spider):
    name = 'crawl_news'
    url_format = "https://search.naver.com/search.naver?where=news&query={0}&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={1}&de={2}&docid=&nso=so%3Ar%2Cp%3Afrom{3}to{4}%2Ca%3Aall&mynews=0&refresh_start={5}1&related=0"
            
    def __init__(
        self, keyword="", start="", end=""
        ):

        dot_start_date = start[:4] + '.' + start[4:6] + '.' + start[6:]
        dot_end_date = end[:4] + '.' + end[4:6] + '.' + end[6:]
        self.start_urls = [self.url_format.format(keyword, dot_start_date,dot_end_date, start, end,0)]
        # self.start_urls = []
        # for i in range(400):
        #     self.start_urls.append(self.url_format.format(keyword, dot_start_date,dot_end_date, start, end,i))
    

    def parse(self, response):
 
        for item in response.css("ul.list_news div.news_info div") :
            url = item.css("a::attr(href)")[1].get()
            print(url)
            yield scrapy.Request(url, callback=self.parse_detail)
               
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):   
        item = NewsCrawlItem()

        item['url']=response.url
        item['title']=response.css("h3#articleTitle::text").get()
        item['media']=response.css("div.press_logo img::attr(title)").get()
        item['date']=response.css("div.sponsor span.t11::text").get()
        item['content']=''.join(response.css("div#articleBodyContents::text").getall()).replace("\n","").strip()

        yield item
