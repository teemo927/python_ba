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
        print('parser')
        if response is None:
            return None
        soup = BeautifulSoup(response, 'html.parser')
        self._get_detail_p(soup)
        # return self._get_detail_p(soup)

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
    1
    <table width="100%" border="0" cellpadding="0" cellspacing="1" bgcolor="#000000">
    """

    def _get_detail_p(self, soup):
        tables = soup.findAll('table', cellpadding='0', cellspacing='1')
        if tables is None:
            print('tables empty')
            return
        for table in tables:
            trs = table.findAll('tr')
            if trs is None:
                print('trs empty')
                return
            for tr in trs:
                tds = tr.findAll('td')
                if tds is None:
                    print('tds empty')
                    return
                for td in tds:
                    text = td.get_text()
                    print("---", text, "\n")
        print('end')
