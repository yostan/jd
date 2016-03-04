# -*- coding: utf-8 -*-


import urllib2
import threading


inFile = open("hdl.txt", "r")
outFile = open("../jd/spiders/proxyok.py", "w")
url = 'http://www.jd.com/'
lock = threading.Lock()
items = []

def check():

    lock.acquire()
    line = inFile.readline().strip()
    # print(line)
    lock.release()

    protocol, proxy = line.split("=")
    # cookie = ""

    try:
        proxyHandle = urllib2.ProxyHandler({protocol.lower(): '://'.join(line.split("="))})
        opener = urllib2.build_opener(proxyHandle, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        # req.add_header("cookie", cookie)
        content = urllib2.urlopen(req, timeout=5).read()
        if len(content) >= 1000:
            lock.acquire()
            print("add proxy: {0}".format(proxy))
            items.append(proxy)
            # outFile.write('{0}\n'.format(proxy))
            lock.release()
        else:
            print("IP Invaild: {0}".format(proxy))
    except Exception, error:
        print("Connection ERR: {0}".format(error))

def writeFile():
    outFile.write("PROXIES = [")
    for item in items:
        outFile.write('\"{0}\",\n'.format(item))
    outFile.write("]")

if __name__ == "__main__":
    threads = []
    for i in range(0,61):
        t = threading.Thread(target=check)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    writeFile()
    inFile.close()
    outFile.close()