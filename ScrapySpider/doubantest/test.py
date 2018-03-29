#!/usr/bin/env python
# coding:utf-8

import requests

html = requests.get("https://movie.douban.com/top250").content
print html.decode("utf-8")

f = open("")