#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 16:46
# @Author  : zhujinghui
# @File    : min0.py
# @Software: PyCharm
import os
import pytesseract
from PIL import Image

image = Image.open(r'D:\PycharmProjects\tasks\xueqiu_scrapy_redis\test\1.png')
vcode = pytesseract.image_to_string(image)

print (vcode)