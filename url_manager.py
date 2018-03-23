#!/usr/bin/env python
# coding:utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加一个新的 URL
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and \
           url not in self.old_urls:
           self.new_urls.add(url)
    
    # 添加一组新 URL
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    # 判断管理器中是否有新爬取的 URL
    def has_new_rul(self):
        return len(self.new_urls) != 0

    # 从管理器中得到新的 URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    
