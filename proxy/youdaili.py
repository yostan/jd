# -*- coding: utf-8 -*-

import re
import requests


def getIP():
    file = open("ydl.txt", "w")
    url = "http://www.youdaili.net/Daili/guonei/4157"

    for page in range(1,3):
        if page == 1:
            rurl = url + ".html"
        else:
            rurl = url + "_{0}.html".format(page)

        html = requests.get(rurl).text
        res = re.findall(r"\d+\.\d+\.\d+\.\d+:\d+", html)
        for ip in res:
            file.write("http={0}\n".format(ip))
            print ip
    file.close()

if __name__ == "__main__":
    getIP()