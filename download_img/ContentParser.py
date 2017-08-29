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
    <div class="threadlist_title pull_left j_th_tit  member_thread_title_frs ">
        <a href="/p/5267439732" title="深夜寂寞有没有小哥哥一起来玩耍的啊" target="_blank" class="j_th_tit " clicked="true">深夜寂寞有没有小哥哥一起来玩耍的啊</a>
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
        tmp_lists = []
        current_page = None
        next_page_url = None
        current_page_t = soup.find('div', class_='pagination-default clearfix')
        if current_page_t is not None:
            current_page = current_page_t.find('span', class_='pagination-current pagination-item ').get_text()
            next_page_url_t = current_page_t.find('a', class_='next pagination-item ')
            if next_page_url_t is not None:
                next_page_url = next_page_url_t.get('href')
        print('current page:', current_page, ',next_page:', next_page_url)
        all_p = soup.findAll('div', class_='threadlist_title pull_left j_th_tit ')
        member_p = soup.findAll('div', class_='threadlist_title pull_left j_th_tit  member_thread_title_frs ')
        for a in all_p:
            tmp_lists = []
            href = a.find('a').get('href')
            title = a.find('a').get_text()
            tmp_lists.append(title)
            tmp_lists.append(href)
            p_lists.append(tmp_lists)
        for a in member_p:
            tmp_lists = []
            href = a.find('a').get('href')
            title = a.find('a').get_text()
            tmp_lists.append(title)
            tmp_lists.append(href)
            p_lists.append(tmp_lists)

        return p_lists, next_page_url, current_page

    """
    解析具体某一个帖子https://tieba.baidu.com/p/5195503800数据
    <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=d56ee320ae0f4bfb8cd09e5c334e788f/b82fd5d2fd1f4134c06689c12f1f95cad0c85eea.jpg" size="57164" changedsize="true" width="560" height="420">
    <li class="l_reply_num" style="margin-left:8px">
        <span class="red" style="margin-right:3px">11</span>回复贴，共
        <span class="red">1</span>页
    </li>
    <li class="l_pager pager_theme_5 pb_list_pager">
        <span class="tP">1</span>
        <a href="/p/1007487363?pn=2">2</a>
        <a href="/p/1007487363?pn=3">3</a>
        <a href="/p/1007487363?pn=4">4</a>
        <a href="/p/1007487363?pn=5">5</a>
        <a href="/p/1007487363?pn=6">6</a>
        <a href="/p/1007487363?pn=2">下一页</a>
        <a href="/p/1007487363?pn=29">尾页</a>
    </li>
    """

    def _get_detail_p(self, soup):
        # 缩略图url
        small_urls = []
        # 原图url
        big_urls = []
        # 原图前缀
        base = 'http://imgsrc.baidu.com/forum/pic/item/'

        total_num = 1
        reply_num = soup.find('li', class_='l_reply_num')
        if reply_num is not None:
            nums = reply_num.findAll('span')
            total_num = nums[-1].get_text()

        img_links = soup.findAll('img', class_='BDE_Image')
        for link in img_links:
            small = link.get('src')
            small_urls.append(small)

            link = str(small)
            name = link.split('/')
            big = base + (name[-1])
            big_urls.append(big)
        small_urls.reverse()
        big_urls.reverse()
        return small_urls, big_urls, total_num
