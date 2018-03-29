#!/usr/bin/env python
# coding:utf-8

from url_manager import UrlManager
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from html_outputer import HtmlOutputer

class SpiderMain():
    def __init__(self):
        # URL 管理器
        # self.urls = UrlManager.UrlManager()
        self.urls = UrlManager()
        # URL 下载器
        # self.downloader = HtmlDownloader.HtmlDownloader()
        self.downloader = HtmlDownloader()
        # URL 解析器
        # self.parser = html_parser.HtmlParser()
        self.parser = HtmlParser()
        # self.outputer = html_outputer.HtmlOutputer()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        originSet = set();
        originSet.add(root_url)
        self.urls.add_new_urls(originSet)
        while self.urls.has_new_rul():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.downloader(new_url)
                
                # 输出信息
                downStat = "ERROR"
                if html_cont != None:
                    downStat = "SUCCESS"
                    print "[Page ID : %d downloader %s!]" % (count, downStat)
                
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                # print "\nnew_urls[%s], new_data[%s]" % (new_urls, new_data)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 15:
                    break
                count = count + 1
            except Exception as err:
                print "craw failed! ERROR infomation : %s" % err
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    
