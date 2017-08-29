#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
爬取指定链接的图片 http://tieba.baidu.com/p/2166231880
"""
import re
from urllib.parse import quote

from ContentParser import ContentParser
from HttpDownloader import HttpDownloader
from UrlManager import UrlManager


class MainSearch(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HttpDownloader()
        self.parser = ContentParser()

    def process_page(self, name_id):
        solo_ba = 'http://weixin.sogou.com/weixin'
        url = solo_ba + name_id
        response = self.downloader.download(url)
        a = self.parser.parser_solo_ba(response)
        if a is None:
            return
        p_lists, next_page, current_page = a

        print('Page:', current_page, ', ListSize：', len(p_lists))
        if len(p_lists) > 0:
            for p in p_lists:
                self.process_article(p)
        if next_page is not None:
            self.process_page(next_page)

    def process_article(self, url):
        self.manager.save_url(url)
        while self.manager.has_url():
            next_url = self.manager.next_url()
            print('detail_article :', next_url)
            response = self.downloader.download(next_url)
            self.parser.parser_detail_p(response)


def include_chinese(text):
    if re.match('[\u4e00-\u9fa5]*', text):
        return True
    else:
        return False


def filter_url(k):
    if not include_chinese(k):
        result = '?type=2&query=' + k
        return result

    result = '?type=2&query='
    for k in kw:
        if include_chinese(k):
            temp = quote(k, safe='/:?=')
            result = result + temp
            print(k, '\n附加不转换字符参数：\n%s' % temp)
        else:
            temp = k
            result = result + temp
    return result


if __name__ == '__main__':
    # http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%8C%BA%E5%9D%97%E9%93%BE&ie=utf8&_sug_=n&_sug_type_=

    main = MainSearch()
    kw = input('请输入微信搜索关键词:')
    kw = filter_url(kw)
    print(kw)
    main.process_page(kw)
