#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UrlManager(object):
    def __init__(self):
        self.urls = []
        self.old_url = []

    def has_url(self):
        return self.urls

    def next_url(self):
        if not self.has_url():
            print('do not have more url')
            return
        else:
            next_url = self.urls.pop()
            self.old_url.append(next_url)
            return next_url

    def save_url(self, url):
        if self.urls.__contains__(url) or self.old_url.__contains__(url):
            print('already contains url :', url)
        else:
            self.urls.append(url)
