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
    解析具体某页列表
    1 打开某个帖子
    <div class="txt-box">
        <h3>
        <a target="_blank" href="" id="sogou_vr_11002601_title_2" uigs="article_title_2"><em><!--red_beg-->区块链<!--red_end--></em>-下一代智能经济的基础信用协议</a>
        </h3>
    </div>
    2 下一页3当前页
    <div class="p-fy" id="pagebar_container">
        <span>1</span>
        <a id="sogou_page_2" href="?query=%E5%8C%BA%E5%9D%97%E9%93%BE&amp;type=2&amp;page=2&amp;ie=utf8" uigs="page_2">2</a>
        <a id="sogou_next" href="?query=%E5%8C%BA%E5%9D%97%E9%93%BE&amp;type=2&amp;page=2&amp;ie=utf8" class="np" uigs="page_next">下一页</a>
        <div class="mun">找到约14,108条结果<!--resultbarnum:14,108--></div>
    </div>
    """

    def _get_solo_ba(self, soup):
        t_current_page = soup.find('div', class_='p-fy').find('span')
        current_page = ''
        if t_current_page is not None:
            current_page = t_current_page.get_text()
        temp_np = soup.find('div', class_='p-fy').find('a', class_='np')
        next_page = None
        if temp_np is not None:
            next_page = temp_np.get('href')
        print('current page:', current_page, ', next_page:', next_page)

        p_lists = []
        all_p = soup.findAll('div', class_='txt-box')
        if all_p is not None:
            for a in all_p:
                href = a.find('a').get('href')
                p_lists.append(href)

        return p_lists, next_page, current_page

    """
    解析具体某一个帖子https://tieba.baidu.com/p/5195503800数据
    <div id="img-content">
        <h2 class="rich_media_title" id="activity-name">
                    区块链和工业4.0：人类的终极风口还是终极骗局？                                    
        </h2>
    </div>
    """

    def _get_detail_p(self, soup):

        temp = soup.find('h2', class_='rich_media_title')
        if temp is not None:
            title = temp.get_text()
            print(title)
        else:
            print("未读取到标题")
