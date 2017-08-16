#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
import urllib.parse

from bs4 import BeautifulSoup


class ContentParser(object):
    def parser_solo_ba(self, response):
        if response is None:
            return None
        soup = BeautifulSoup(response, 'html.parser')
        return self._get_solo_ba(soup)

    def parser_detail_p(self, response):
        if response is None:
            return None
        soup = BeautifulSoup(response, 'html.parser')
        return self._get_detail_p(soup)

    """"
    解析具体某个贴吧
    1 打开某个帖子
    <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-top" alt="置顶" title="置顶"></i><i class="icon-good" alt="精品" title="精品"></i>
    <a href="/p/4982275764" title="希望这是很愉快的一年" target="_blank" class="j_th_tit ">希望这是很愉快的一年</a>
    </div>
    2 下一页
    <div id="frs_list_pager" class="pagination-default clearfix"><span class="pagination-current pagination-item ">1</span>
    <a href="//tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&amp;ie=utf-8&amp;pn=50" class="next pagination-item ">下一页&gt;</a>
    </div>
    3当前页
    <div id="frs_list_pager" class="pagination-default clearfix">
    <span class="pagination-current pagination-item ">1</span>
    """

    def _get_solo_ba(self, soup):
        p_lists = []
        current_page = soup.find('div', class_='pagination-default clearfix').find('span', class_='pagination-current pagination-item')
        next_page = soup.find('div', class_='pagination-default clearfix').find('a', class_='next pagination-item ').get('href')
        print('current page:', current_page, ',next_page:', next_page)
        all_p = soup.findAll('div', class_='threadlist_title pull_left j_th_tit ')
        for a in all_p:
            href = a.find('a').get('href')
            p_lists.append(href)

        return p_lists, next_page, current_page

    """
    解析具体某一个帖子https://tieba.baidu.com/p/5195503800数据
    <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=d56ee320ae0f4bfb8cd09e5c334e788f/b82fd5d2fd1f4134c06689c12f1f95cad0c85eea.jpg" size="57164" changedsize="true" width="560" height="420">
    """

    def _get_detail_p(self, soup):
        # 缩略图url
        small_urls = []
        # 原图url
        big_urls = []
        # 原图前缀
        base = 'http://imgsrc.baidu.com/forum/pic/item/'

        img_links = soup.findAll('img', class_='BDE_Image')
        for link in img_links:
            small = link.get('src')
            small_urls.append(small)

            link = str(small)
            name = link.split('/')
            big = base + (name[-1])
            big_urls.append(big)
        return small_urls, big_urls
