#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import urllib.parse
import urllib.request
from urllib.error import URLError

import requests


class HttpDownloader(object):
    def download(self, url):
        if url is None:
            return None
        print(url)
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.text

    def load_imgs(self, img_urls, title, ba_name, big=False):
        if img_urls is None:
            return None

        index = 0
        for img_url in img_urls:
            path = self._get_path(img_url, title, ba_name, big)
            index = index + 1
            self._load_img(img_url, path, index)

    def _get_path(self, url, title, ba_name, big=False):
        try:
            # sss = str(url_path).split('/')
            name = title
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
        except Exception as e:
            print(e)

    def _load_img(self, img_url, path, index):
        try:
            urllib.request.urlretrieve(img_url, path)
            print(index, '、', img_url)
            print(index, '、', path)
        except URLError as e:
            print(e)
