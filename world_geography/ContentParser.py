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
    1
    解析具体某一个帖子https://zhuanlan.zhihu.com/p/26647066数据
    <div class="PostIndex-header av-paddingTop av-card" data-zop="{&quot;authorName&quot;:&quot;英国报姐&quot;,&quot;itemId&quot;:&quot;26647066&quot;,&quot;title&quot;:&quot;台湾美女作家抑郁自杀，13岁被老师诱奸经历写进小说&quot;,&quot;type&quot;:&quot;article&quot;}">
        <div class="TitleImage">
            <img alt="台湾美女作家抑郁自杀，13岁被老师诱奸经历写进小说" src="https://pic4.zhimg.com/v2-b3512fcbe3f4e5e35e6fb2951a449367_r.png" class="TitleImage-imagePure TitleImage-imagePure--fixed" height="597px">
        </div>
        <h1 class="PostIndex-title av-paddingSide av-titleFont">台湾美女作家抑郁自杀，13岁被老师诱奸经历写进小说</h1>
    </div>
    
    2
    <div class="RichText PostIndex-content av-paddingSide av-card">
    </div>
    
    3
    <a href="/p/26647112" class="PostListItem-titleImageWrapper">
        <img src="https://pic1.zhimg.com/v2-8633dc13e328f24a6285a166000ee290_b.png" class="PostListItem-titleImage" alt="题图">
    </a>
    返回文章标题、所有图片、相关文章链接('/p/26647112')
    """

    def _get_detail_p(self, soup):
        # 'https://zhuanlan.zhihu.com/p/26647066'
        title = ''
        img_urls = []
        p_lists = []

        title_t = soup.find('div', class_='PostIndex-header av-paddingTop av-card')
        if title_t is not None:
            title_img = title_t.find('img').get('src')
            img_urls.append(title_img)
            title = title_t.find('h1').get_text()

        img_links = soup.findAll('div', class_='RichText PostIndex-content av-paddingSide av-card')
        for link in img_links:
            small = link.get('src')
            img_urls.append(small)

        p_list_t = soup.findAll('a', class_='PostListItem-titleImageWrapper')
        for p_t in p_list_t:
            p = p_t.find('img').get('src')
            p_lists.append(p)

        img_urls.reverse()
        p_lists.reverse()
        return title, img_urls, p_lists
