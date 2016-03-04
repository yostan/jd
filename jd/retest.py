# -*- coding: utf-8 -*-

import re
import math
import json
import codecs
import random
from collections import OrderedDict

def research():
    s = "isClosePCShow: false,venderId:1000004067,shopId:'1000004067',commentVersion:'53129',specialAttrs"
    ss = r'fetchJSON_comment98vv22230({"productAttr":null,"productCommentSummary":"topFiveCommentVos":[]});'
    p = re.compile(r"commentVersion:'(\d+)'", re.IGNORECASE)
    pp = re.compile(r"fetchJSON_comment98vv[\d]+\((.*)", re.IGNORECASE)
    res1 = p.search(s).group(1)
    res2 = pp.search(ss).group(1)[:-2]
    print("result1: {0}".format(res1))
    print("result2: {0}".format(res2))
    print(int(math.ceil(2111 / 10.0)))

def jsontest():
    items = []
    it1 = {}
    it1["aa"] = 1
    it1["dd"] = u'\u91d1\u724c\u4f1a\u5458'
    it2 = {}
    it2["ww"] = u'\u5305\u88c5\u4e0d\u662f\u5f88\u597d'
    it2["qq"] = 4
    # it2["ss"] = u'2009-07-05 19:47:31'
    items.append(it1)
    items.append(it2)

    print(dict(items[0]))


    file = codecs.open('test001.json', 'a', encoding='utf-8')
    line = json.dumps(it2, ensure_ascii=False, sort_keys=False) + "\n"
    # print(line)
    file.write(line)


def testIP():
    ips = ["192.168.1.1:8080","192.168.1.2:8080","192.168.1.3:8080","192.168.1.4:8080","192.168.1.5:8080"]
    for i in range(10):
        ip = random.choice(ips)
        print(ip)

if __name__ == "__main__":
    # jsontest()
    testIP()