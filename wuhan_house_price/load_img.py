#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
爬取指定链接的图片 http://tieba.baidu.com/p/2166231880
"""
from ContentParser import ContentParser
from HttpDownloader import HttpDownloader
from UrlManager import UrlManager


class Main(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HttpDownloader()
        self.parser = ContentParser()

    def process_solo(self, name_id, fold):
        # next_page: //tieba.baidu.com/f?kw=%E5%A5%B3%E4%BA%BA&ie=utf-8&pn=50
        solo_ba = 'https:'
        url = solo_ba + name_id

        response = self.downloader.download(url)
        p_lists, next_page, current_page = self.parser.parser_solo_ba(response)

        print('第', current_page, '页帖子，', 'next_page：', next_page, p_lists)
        for p in p_lists:
            self.process_p(p[0], p[1], fold)
        if next_page is not None:
            self.process_solo(next_page, fold)
        else:
            print('HAPPY!  program finish!!!!!')

    def process_p(self, page):
        # http://scxx.whfcj.gov.cn/xmqk.asp?page=1
        base_url = 'http://scxx.whfcj.gov.cn/xmqk.asp?page='
        url = base_url + str(page)

        self.manager.save_url(url)
        while self.manager.has_url():
            next_url = self.manager.next_url()
            print('detail_p :', next_url)
            response = self.downloader.download(next_url)
            self.parser.parser_detail_p(response)


if __name__ == '__main__':
    main = Main()
    init_page = 1
    main.process_p(init_page)

