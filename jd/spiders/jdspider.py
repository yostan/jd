# -*- coding: utf-8 -*-

import re
import json
import math
from scrapy import Spider,Request
from jd.items import JdItem, CommentsItem


class JdSpider(Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    #phone cat: 9987,653,655
    base_url = r"http://list.jd.com/list.html?cat=%s&go=0"
    page = "&page=%d"

    maxpage_css = ".f-pager .fp-text i::text"
    item_css = ".gl-i-wrap.j-sku-item .p-img a::attr(href)"

    def __init__(self, cat="9987,653,655", *args, **kwargs):
        super(JdSpider, self).__init__(*args, **kwargs)
        self.cat = cat
        self.start_urls = []
        self.max_page = None


    def start_requests(self):
        print("start request ------")
        return [Request(self.base_url % self.cat, callback=self.get_max_page)]


    def get_max_page(self, response):
        maxpage = response.css(self.maxpage_css).extract()
        print("max page: {0}".format(maxpage[0]))
        self.max_page = int(maxpage[0])
        # yield Request(response.url, callback=self.parse)
        for i in range(1,2):
            yield Request(response.url + self.page % i, callback=self.get_items)


    def get_items(self, response):
        jdItem = JdItem()
        jdItem["itemUrl"] = "http://item.jd.com/1856581.html"
        jdItem["id"] = "1856581"
        yield Request("http://item.jd.com/1856581.html", meta={'jdItem': jdItem}, callback=self.get_commentVersion)
        # print("get page: %s", response.url)
        # progress = open("progress.txt", mode="r")
        # for itemurl in response.css(self.item_css).extract():
        #     p = re.compile(r"http://item.jd.com/(\d+).html", re.IGNORECASE)
        #     id = p.search(itemurl).group(1)
        #     jdItem = JdItem()
        #     jdItem["itemUrl"] = itemurl
        #     jdItem["id"] = id
        #     # response.meta["jdItem"] = jditem
        #     yield Request(itemurl, meta={'jdItem': jdItem}, callback=self.get_commentVersion)


    def get_commentVersion(self, response):
        commentCount = r"http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds={0}"
        # print("get page: %s", response.url)
        p = re.compile(r"commentVersion:'(\d+)'", re.IGNORECASE)
        commentVersion = p.search(response.body_as_unicode()).group(1)
        jdItem = response.meta["jdItem"]
        itemid = jdItem["id"]
        jdItem["commentVersion"] = commentVersion
        rurl = commentCount.format(itemid)
        yield Request(rurl, meta={'jdItem': jdItem}, callback=self.get_commentCount)


    def get_commentCount(self, response):
        # print("get page: %s", response.url)
        data = json.loads(response.body_as_unicode())
        cc = data["CommentsCount"][0]
        commentCount = cc["CommentCount"]
        jdItem = response.meta["jdItem"]
        itemid = jdItem["id"]
        commentVersion = jdItem["commentVersion"]
        jdItem["commentCount"] = commentCount
        pageNum = int(math.ceil(commentCount / 10.0))
        print("itemid:{0}, commentCount:{1}, pageMum:{2}".format(itemid, commentCount, pageNum))
        for i in range(0, pageNum):
            rurl = r"http://club.jd.com/productpage/p-{0}-s-0-t-5-p-{1}.html?callback=fetchJSON_comment98vv{2}".format(itemid, i, commentVersion)
            yield Request(rurl, meta={'jdItem': jdItem}, callback=self.parse_comments)


    def parse_comments(self, response):
        p = re.compile(r"fetchJSON_comment98vv[\d]+[(](.*)")
        try:
            res = p.search(response.body_as_unicode()).group(1)[:-2]
        except:
            return
        comments = json.loads(res)
        length = len(comments["comments"])
        print("length: {0}".format(length))

        items = []
        for i in range(0, length):
            c = comments["comments"][i]
            commentsItem = CommentsItem()
            commentsItem["userId"] = c["id"]
            commentsItem["content"] = c["content"]
            commentsItem["creationTime"] = c["creationTime"]
            commentsItem["itemId"] = c["referenceId"]
            commentsItem["purchaseTime"] = c["referenceTime"]
            commentsItem["score"] = c["score"]
            commentsItem["userLevelId"] = c["userLevelId"]
            commentsItem["userRegisterTime"] = c["userRegisterTime"]
            commentsItem["userLevelName"] = c["userLevelName"]
            commentsItem["isMobile"] = c["isMobile"]
            commentsItem["days"] = c["days"]
            items.append(commentsItem)
        return items
