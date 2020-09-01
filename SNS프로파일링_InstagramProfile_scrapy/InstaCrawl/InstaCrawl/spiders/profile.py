import re, requests, json, urllib, datetime, scrapy, time
import pandas as pd
from InstaCrawl.items import InstacrawlItem

class InstaProfileSpider(scrapy.Spider):
    name = 'profile'
    headers = {'cookie' : 'ig_did=6A142BE8-A4FA-4BCB-A15F-C41E2F7CF2BA; mid=Xz9q9wALAAHsdxymIjepqNOBeS-k; fbm_124024574287414=base_domain=.instagram.com; csrftoken=j343qU4IkTVg3S6WtJYPqEdLQkjdspmw; ds_user_id=6769785738; sessionid=6769785738%3AwyRKkIho2qI1Zu%3A2; shbid="8668\0546769785738\0541630507157:01f74fd177d1c380175ef3524de37ad2fa9b454e45db764f6d83432dbd55664cde4285dc"; shbts="1598971157\0546769785738\0541630507157:01f7a3b0b0ebae54cbee5f000f895f0ca63c685fa75f0b4b1562192068a2aa58ad794b30"; rur="VLL\0546769785738\0541630507165:01f73c0de264eb816ca7eb4e8c98aea55b3de89817428e46f0a1866e630bbba592afe3df"; urlgen="{\"211.201.31.104\": 9318}:1kD7RV:WRjx-LyLvQyUl585BZbmBdUKCEo"',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                }
    # allowed_domains = ['instagram.com']
    # start_urls = ['http://instagram.com/']
    # url_format = 'https://www.instagram.com/{0}/?__a=1'
    crawling_count = 0
    def __init__(self,file):
        insta_ids = list(pd.read_csv(file, header=None)[0])
        first_url = 'https://www.instagram.com/{0}/?__a=1'
        self.urls = []
        for insta_id in insta_ids:
            self.urls.append(first_url.format(insta_id))

    def start_requests(self) :
        for url in self.urls :
            yield scrapy.Request(url=url, headers=InstaProfileSpider.headers, callback=self.parse, encoding='utf-8')


    def parse(self, response):
        result_dic = json.loads(response.text)
        item = InstacrawlItem()
        for i in range(len(result_dic['data']['user']['reel']['user']['username'])):
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