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

    def process_p(self, short_url):
        # https://zhuanlan.zhihu.com/p/26647066
        base_url = 'https://zhuanlan.zhihu.com'
        url = base_url + short_url

        self.manager.save_url(url)
        while self.manager.has_url():
            next_url = self.manager.next_url()
            print('detail_p :', next_url)
            response = self.downloader.download(next_url)
            print(response)
            title, img_urls, links = self.parser.parser_detail_p(response)
            if title is not None and img_urls is not None:
                self.downloader.load_imgs(title, img_urls)
            if links is not None:
                self.manager.save_urls(links)


if __name__ == '__main__':
    main = Main()
    # type = input('start type:')

    # name_id = input('请输入贴吧名字（如：https://tieba.baidu.com/f?ie=utf-8&kw=good  则输入 good）:')
    # solo_ba = '//tieba.baidu.com/f?kw='
    # main.process_solo(solo_ba + name_id, name_id)

    name_id = input('请输入知乎ID号（如：https://zhuanlan.zhihu.com/p/26647066则输入26647066）:')
    main.process_p("/p/" + name_id)

    content = '\u53f0\u6e7e\u6700\u7f8e\u7684\u98ce\u666f\u662f\u4eba\uff0c\u7b97\u4e0d\u7b97\u5403\u4eba\u8840\u9992\u5934\u3002'
    print(content)
