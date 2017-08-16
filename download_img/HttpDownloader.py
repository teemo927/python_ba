#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import urllib.request
import urllib.parse

import os
from urllib.error import URLError


class HttpDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
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
            self._load_img(img_url, path, index)

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

    def _load_img(self, img_url, path, index):
        try:
            urllib.request.urlretrieve(img_url, path)
            print(index, '、', img_url)
            print(index, '、', path)
        except URLError as e:
            print(e)
