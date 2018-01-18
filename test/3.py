#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 15:46
# @Author  : zhujinghui
# @File    : 3.py
# @Software: PyCharm
import requests
import feedparser
url1 = "https://www.sec.gov/cgi-bin/srch-edgar?text=FILING-DATE%3D%2020171011&start=1&count=3000&first=2016&last=2017&output=atom"
url2 = "https://www.sec.gov/cgi-bin/srch-edgar?text=FILING-DATE%3D%2020171011&start=101&count=3000&first=2016&last=2017&output=atom"

#
# rsp = requests.get(url)
# print(rsp.text)

d1 = feedparser.parse(url1)
d2 = feedparser.parse(url2)

print(d1['entries'][0])
print(d2['entries'][0])