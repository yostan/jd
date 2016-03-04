# -*- coding:utf-8 -*-

import requests
from lxml import etree

url = "http://weibo.cn/u/1890493665"
url_login = "https://login.weibo.cn/login/"

html = requests.get(url).content
selector = etree.HTML(html)

passwd = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]

print action
print passwd
print vk

new_url = url_login + action
data = {
    'mobile': '',
    'password': '',
    'remember': 'on',
    'backURL': url,
    'backTitle': u'微博',
    'tryCount': '',
    'vk': vk,
    'submit': u'登录'
}

newhtml = requests.post(new_url, data=data).content
new_selector = etree.HTML(newhtml)

content = new_selector.xpath('//span[@class="ctt"]')
for t in content:
    text = t.xpath('string(.)')
    print text


