# -*- coding: utf-8 -*-

import re
import requests
import time
from lxml import etree


def getIP():
    file = open("hdl.txt", "w")
    url = "http://www.haodailiip.com/guonei/"

    for page in range(1,3):
        rurl = url + str(page)
        print(rurl)

        html = requests.get(rurl).text

        tree = etree.HTML(html)
        ipList = tree.xpath('//table[@class="proxy_table"]/tr')
        print(len(ipList))

        for item in ipList[1:]:
            ip = item.xpath('td[1]')[0].text.strip()
            port = item.xpath('td[2]')[0].text.strip()
            print("{0}:{1}".format(ip, port))
            file.write("http={0}:{1}\n".format(ip, port))
        time.sleep(2)
    file.close()


if __name__ == "__main__":
    getIP()