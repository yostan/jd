# -*- coding: utf-8 -*-


import urllib2
import threading
from lxml import etree


def getIp():
    file = open("xici.txt", "w")
    for page in range(1, 3):
        url = "http://www.xicidaili.com/nn/{0}".format(page)
        print(url)
        ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        req = urllib2.Request(url)
        req.add_header("User-Agent", ua)
        resp = urllib2.urlopen(req)

        tree = etree.HTML(resp.read())

        ipList = tree.xpath('//table[@id="ip_list"]/tr')
        print(len(ipList))

        for item in ipList[1:]:
            ip = item.xpath('td[3]')[0].text
            port = item.xpath('td[4]')[0].text
            protocol = item.xpath('td[7]')[0].text
            if protocol == "HTTP" or protocol == "HTTPS":
                file.write("{0}={1}:{2}\n".format(protocol.lower(), ip, port))
                print("{0}://{1}:{2}".format(protocol, ip, port))
    file.close()


if __name__ == "__main__":
    getIp()