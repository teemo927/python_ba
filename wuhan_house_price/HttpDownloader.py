#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import urllib.parse
import urllib.request
from urllib.error import URLError

from Proxy_Get import Proxy_Get


class HttpDownloader(object):
    def download(self, url):
        if url is None:
            return None
        print(url)
        p = Proxy_Get()
        res = p.proxy_url(url)
        print(res)
        return res

    def load_imgs(self, title, img_urls):
        if img_urls is None:
            return None

        for index in range(len(img_urls)):
            img_url = img_urls[index]
            path = self._get_path(index, title, img_url)
            self._load_img(img_url, path, index)

    def _get_path(self, url, title, index):
        try:
            base = os.getcwd() + "\\py_downloads\\" + title + "\\"
            if os.path.exists(base) is False:
                os.makedirs(base)
            link = str(url)
            name = link.split('/')
            path = base + str(index) + "_" + name[-1]
            if path.__contains__('&'):
                path = str(path).split('&')[-1]

            return path
        except Exception as e:
            print(e)

    def _load_img(self, img_url, path, index):
        try:
            urllib.request.urlretrieve(img_url, path)
            print(index, '、', img_url)
            print(index, '、', path)
        except URLError as e:
            print(e)
