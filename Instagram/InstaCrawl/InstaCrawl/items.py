# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstacrawlItem(scrapy.Item):
    login_id = scrapy.Field()
    profile = scrapy.Field()
    follower = scrapy.Field()
    following = scrapy.Field()