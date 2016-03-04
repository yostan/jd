# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    itemUrl = scrapy.Field()
    id = scrapy.Field()
    commentVersion = scrapy.Field()
    commentCount = scrapy.Field()


class CommentsItem(scrapy.Item):
    userId = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    itemId = scrapy.Field()
    purchaseTime = scrapy.Field()
    score = scrapy.Field()
    userLevelId = scrapy.Field()
    userRegisterTime = scrapy.Field()
    userLevelName = scrapy.Field()
    isMobile = scrapy.Field()
    days = scrapy.Field()




