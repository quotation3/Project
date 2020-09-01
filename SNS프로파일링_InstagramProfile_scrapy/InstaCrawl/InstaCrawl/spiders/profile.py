import re, requests, json, urllib, datetime, scrapy, time
import pandas as pd
from InstaCrawl.items import InstacrawlItem

class InstaProfileSpider(scrapy.Spider):
    name = 'profile'
    # allowed_domains = ['instagram.com']
    # start_urls = ['http://instagram.com/']
    url_format = 'https://www.instagram.com/{0}/?__a=1'
    crawling_count = 0
    def __init__(self, file):
        user_id = list(pd.read_csv(file, header=None)[0])
        self.urls = []
        for user in user_id:
            self.urls.append(InstaProfileSpider.url_format.format(user))

    def start_requests(self) :
        headers = {'cookie' : 'ig_did=6A142BE8-A4FA-4BCB-A15F-C41E2F7CF2BA; mid=Xz9q9wALAAHsdxymIjepqNOBeS-k; fbm_124024574287414=base_domain=.instagram.com; csrftoken=CUGmV4SAGEvIs0jKbZYCwKLd9K4dMByo; ds_user_id=40522214037; sessionid=40522214037%3AhX2ctZmEqZhDgC%3A1; rur="VLL\05440522214037\0541630469700:01f774cc7c8f9476b6b487998a43faa8ca4ae3c2009b39c69ce2022655f725c7af6db732"; urlgen="{\"211.201.31.104\": 9318}:1kCxhE:sXAPKw0BRbhDSaHvHOYYNOFqe8M"',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                }
        for url in self.urls :
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
            # yield Request(item['link'],meta = {
            #       'dont_redirect': True,
            #       'handle_httpstatus_list': [302]
            #   }, callback=self.your_callback)

    def parse(self, response):
        result_dic = json.loads(response.text)
        item = InstacrawlItem()
        for i in range(len(result_dic['data']['user']['reel']['user']['username'])):
        #     # 크롤링 횟수 카운트
            self.crawling_count  += 1
            if self.crawling_count % 200 == 0:
                time.sleep(300)

            print("*"*50)
            print(result_dic['graphql']['user']['username'])
            print(result_dic['graphql']['user']['biography'])
            item['usename'] = result_dic['graphql']['user']['username']
            item['profile'] = result_dic['graphql']['user']['biography']
            item['follower_cnt'] = result_dic['graphql']['user']['edge_followed_by']['count']
            item['following_cnt'] = result_dic['graphql']['user']['edge_follow']['count']

            yield item