#!/usr/bin/env python
# coding:utf-8

import lxml.html
import chardet
import requests 
from bs4 import BeautifulSoup

source = u"""
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="test">我需要的信息2</li>
        <li class="iamstrange">我需要的信息3</li>
      </ul>
     </div>
     <div class="useful">
      <ul>
        <li class="info">A1</li>
        <li class="test">A2</li>
        <li class="iamstrange">A3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>
"""

soup = BeautifulSoup(source, "html.parser")
useful = soup.find_all("div", class_="useful")
print useful
