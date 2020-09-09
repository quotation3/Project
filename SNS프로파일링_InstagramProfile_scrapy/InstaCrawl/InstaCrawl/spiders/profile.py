import re, requests, json, urllib, datetime, scrapy, time
import pandas as pd
from InstaCrawl.items import InstacrawlItem
from InstaCrawl.middlewares import TooManyRequestsRetryMiddleware

class InstaProfileSpider(scrapy.Spider):
    name = 'profile'
    # headers = { 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    #             }

    # headers = { 'x-instagram-gis': 'ad034c3799ec2a9b083be2bbb257ffec',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
             

    # cookies = {'ig_did':'6A142BE8-A4FA-4BCB-A15F-C41E2F7CF2BA',
    # 'mid': 'Xz9q9wALAAHsdxymIjepqNOBeS-k', 
    # 'fbm_124024574287414':'base_domain=.instagram.com',
    # 'shbid':'8668\0546769785738\0541630507157:01f74fd177d1c380175ef3524de37ad2fa9b454e45db764f6d83432dbd55664cde4285dc',
    # 'shbts':'1598971157\0546769785738\0541630507157:01f7a3b0b0ebae54cbee5f000f895f0ca63c685fa75f0b4b1562192068a2aa58ad794b30', 
    # 'csrftoken':'F7NFJ4LI2PfrKsuoZ7r50sfuJYTh7UEC', 
    # 'ds_user_id': '40522214037; sessionid=40522214037%3AX7mewGdkcbhJdg%3A6',
    # 'rur':'VLL\05440522214037\0541630547219:01f73e9a04ab794a0aadf6dc1a3489b97c65db51dec5338cee6278821057322646fc586e',
    # 'urlgen':'{\"211.201.31.104\": 9318}:1kDHrX:OlPxhUGurPPaaZbyp0fhkyj-wjQ'}

    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    cookies = {'ig_did' : '163B7911-4E71-4B66-8D0F-667BBC63BE31',
    'mid' : 'X00kegALAAGzZJLgu2_D7CBeq6gS',
    'shbid' : '8668\0546769785738\0541631030369:01f7e1e27d3444b97f31b997209553a8458b02f7bc55369288996153880a642223ce1a44',
    'shbts' : '1599494369\0546769785738\0541631030369:01f785ae10206300ffad6068ffe3237a76197c21e18dd094fd96939e902b5d690b28b00c',
    'csrftoken' : 'bVPmfbYJ3YkcxkIBecSPD2GSqBKNk4f3',
    'rur' : 'PRN',
    'ds_user_id' : '41192186578',
    'sessionid' : '41192186578%3AFlrhRO4oTR3XRG%3A5',
    'urlgen' : '{\"61.105.2.105\": 9318}:1kFdNU:HzARLVucpdfVUOSM0XP687vL-8Y'}

    allowed_domains = ['instagram.com']
    start_urls = ['http://instagram.com/']
    url_format = 'https://www.instagram.com/{0}/?__a=1'
    crawling_count = 0
    def __init__(self,file):
        insta_ids = list(pd.read_json(file)['username'][1302:])
        first_url = 'https://www.instagram.com/{0}/?__a=1'
        self.urls = []
        for insta_id in insta_ids:
            self.urls.append(first_url.format(insta_id))

    def start_requests(self) :
        for url in self.urls :
            yield scrapy.Request(url=url, meta={'dont_redirect':True}, headers=InstaProfileSpider.headers, cookies = InstaProfileSpider.cookies, callback=self.parse)


    def parse(self, response):
        #print(response.text)
        result_dic = json.loads(response.text)
        item = InstacrawlItem()
        self.crawling_count  += 1
        if self.crawling_count % 270 == 0:
            time.sleep(1000)

        #print("*"*50)
        #print(result_dic['graphql']['user']['username'])
        #print(result_dic['graphql']['user']['biography'])
        item['username'] = result_dic['graphql']['user']['username']
        item['profile'] = result_dic['graphql']['user']['biography']
        item['follower_cnt'] = result_dic['graphql']['user']['edge_followed_by']['count']
        item['following_cnt'] = result_dic['graphql']['user']['edge_follow']['count']

        yield item