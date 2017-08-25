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
        self.num = 1

    def process_solo(self, name_id):
        # https://tieba.baidu.com/f?kw=no
        solo_ba = 'https://tieba.baidu.com/f?kw='
        url = solo_ba + name_id
        response = self.downloader.download(url)
        p_lists, next_page, current_page = self.parser.parser_solo_ba(response)

        print('第', current_page, '页帖子：', p_lists)
        for p in p_lists:
            self.process_p(p[0], p[1], name_id)
        if next_page is not None:
            self.process_solo(next_page)

    def process_p(self, title, short_url, ba_name):
        # http://tieba.baidu.com/p/5287680253
        base_url = 'http://tieba.baidu.com'
        url = base_url + short_url +"?pn=" + str(self.num)

        self.manager.save_url(url)
        while self.manager.has_url():
            next_url = self.manager.next_url()
            print('detail_p :', next_url)
            response = self.downloader.download(next_url)
            new_img_urls, big_img_urls = self.parser.parser_detail_p(response)

            # 'http://imgsrc.baidu.com/forum/pic/item/'
            self.downloader.load_imgs(big_img_urls, title, ba_name,  True)
        self.num = self.num + 1

        if self.num > 10:
            self.num = 1
            return
        else:
            self.process_p(title, short_url, ba_name)


if __name__ == '__main__':

    main = Main()
    name_id = input('请输入贴吧名字（如：https://tieba.baidu.com/f?ie=utf-8&kw=good  则输入 good）:')
    main.process_solo(name_id)

    # name_id = input('请输入贴吧ID号（如：http://tieba.baidu.com/p/1165861759则输入1165861759）:')
    # main.process_p("/p/"+ name_id,name_id)
