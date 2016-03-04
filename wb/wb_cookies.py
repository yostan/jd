# -*- coding:utf-8 -*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool

cookie = {"Cookie": ""}
url = "http://weibo.cn"

html = requests.get(url, cookie = cookie).content
# html = requests.get(url, cookie = cookie).text
# html = bytes(bytearray(html, encoding='utf-8'))

print html

selector = etree.HTML(html)
content = selector.xpath('//span[@class="ctt"]')
for t in content:
    text = t.xpath('string(.)')
    print text
