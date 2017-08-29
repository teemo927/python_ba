#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse

import os
from urllib import request
from urllib.error import URLError


def _load_img(img_url, path, index):
    try:
        urllib.request.urlretrieve(img_url, path)
        print(index, '、', img_url)
        print(index, '、', path)
    except URLError as e:
        print(e)


class HttpDownloader(object):
    def download(self, url):
        head = {}
        # 写入User Agent信息
        head[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
        # head['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        # 创建Request对象
        req = request.Request(url, headers=head)

        # # 这是代理IP
        # proxy = {'http': '139.196.176.18:9797'}
        # # 创建ProxyHandler
        # proxy_support = request.ProxyHandler(proxy)
        # # 创建Opener
        # opener = request.build_opener(proxy_support)
        # # 安装OPener
        # request.install_opener(opener)

        if url is None:
            return None
        response = request.urlopen(req)
        if response.getcode() != 200:
            return None
        return response.read()

    def load_imgs(self, img_urls, name, ba_name, big=False):
        if img_urls is None:
            return None

        index = 0
        for img_url in img_urls:
            path = self._get_path(img_url, name, ba_name, big)
            index = index + 1
            _load_img(img_url, path, index)

    def _get_path(self, url, url_path, ba_name, big=False):
        sss = str(url_path).split('/')
        name = sss[-1]
        if big:
            base = os.getcwd() + "\\py_downloads\\" + ba_name + '\\' + name + "\\"
        else:
            base = os.getcwd() + "\\py_downloads\\" + ba_name + '\\' + name + "\\small\\"
        if os.path.exists(base) is False:
            os.makedirs(base)
        link = str(url)
        name = link.split('/')
        path = base + name[-1]
        if path.__contains__('&'):
            path = str(path).split('&')[-1]

        return path
