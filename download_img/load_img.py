#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
爬取指定链接的图片 http://tieba.baidu.com/p/2166231880
"""
import re
from urllib import parse

from ContentParser import ContentParser
from HttpDownloader import HttpDownloader
from UrlManager import UrlManager


class Main(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HttpDownloader()
        self.parser = ContentParser()
        self.num = 1

    def process_solo(self, name, fold):
        # next_page: //tieba.baidu.com/f?kw=%E5%A5%B3%E4%BA%BA&ie=utf-8&pn=50
        ba = 'https:'
        url = ba + name

        response = self.downloader.download(url)
        p_lists, next_page, current_page = self.parser.parser_solo_ba(response)

        print('第', current_page, '页帖子，', 'next_page：', next_page, p_lists)
        for p in p_lists:
            self.process_p(p[0], p[1], fold)
        if next_page is not None:
            self.process_solo(next_page, fold)
        else:
            print('HAPPY!  program finish!!!!!')

    def process_p(self, title, short_url, ba_name):
        # http://tieba.baidu.com/p/5287680253
        base_url = 'http://tieba.baidu.com'
        if self.num is not 1:
            url = base_url + short_url + "?pn=" + str(self.num)
        else:
            url = base_url + short_url

        self.manager.save_url(url)
        while self.manager.has_url():
            next_url = self.manager.next_url()
            print('detail_p :', next_url)
            response = self.downloader.download(next_url)
            new_img_urls, big_img_urls, total_num = self.parser.parser_detail_p(response)

            # 'http://imgsrc.baidu.com/forum/pic/item/'
            self.downloader.load_imgs(big_img_urls, title, ba_name, True)

            self.num = self.num + 1

            if self.num > int(total_num):
                self.num = 1
                return
            else:
                self.process_p(title, short_url, ba_name)


def checkChinese(name_id):
    # %B5%D4%D0%C0%D0%C0&pn=30
    result = ""
    sss = name_id.split("&")
    name_f = sss[0]
    pattern = re.compile(u'[\u4e00-\u9fa5]')
    for i in name_f:
        print(i)
        if pattern.match(i):
            a = parse.quote(i)
            print("tra--" + a)
            result += a
        else:
            print(i)
            result += i
    if len(sss) > 1:
        result += "&" + sss[1]
    print(result)
    return result, name_f


if __name__ == '__main__':
    main = Main()
    type_in = input('start type:')
    if type_in == "1":
        name_id = input('请输入贴吧名字（如：https://tieba.baidu.com/f?ie=utf-8&kw=good  则输入 good）:')
        name_url, name_fold = checkChinese(name_id)
        solo_ba = '//tieba.baidu.com/f?kw='
        main.process_solo(solo_ba + name_url, name_fold)
    else:
        name_id = input('请输入贴吧ID号（如：http://tieba.baidu.com/p/1165861759则输入1165861759）:')
        main.process_p(name_id, "/p/" + name_id, str(name_id))
