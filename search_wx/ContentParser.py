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
    4 简介
    <div class="txt-box">
        <h3>
        <a target="_blank" href="" id="sogou_vr_11002601_title_2" uigs="article_title_2"><em><!--red_beg-->区块链<!--red_end--></em>-下一代智能经济的基础信用协议</a>
        </h3>
        <p class="txt-info" id="sogou_vr_11002601_summary_0">在互联网金融被质疑,被诟病,被打压的时候,<em><!--red_beg-->区块链<!--red_end--></em>概念适时出现,这一脱胎于比特币的神秘数据处理技术被描述的近乎完美.去中...</p>
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
        d = soup.find('div', class_='p-fy')
        if d is None:
            print(soup)
            return None

        t_current_page = d.find('span')
        current_page = None
        if t_current_page is not None:
            current_page = t_current_page.get_text()

        temp_np = d.find('a', class_='np')
        next_page = None
        if temp_np is not None:
            next_page = temp_np.get('href')
        print('current page:', current_page, ', next_page:', next_page)

        p_lists = []
        all_p = soup.findAll('div', class_='txt-box')
        if all_p is not None:
            for a in all_p:
                href = a.find('a').get('href')
                # abstract = a.find('p', class_='txt-info').get_text()
                p_lists.append(href)

        return p_lists, next_page, current_page

    """
    解析具体某一个帖子https://tieba.baidu.com/p/5195503800数据
    <div id="img-content">
        <h2 class="rich_media_title" id="activity-name">
                    区块链和工业4.0：人类的终极风口还是终极骗局？                                    
        </h2>
        <div id="meta_content" class="rich_media_meta_list">
            <em id="post-date" class="rich_media_meta rich_media_meta_text">2017-07-31</em>
            <em class="rich_media_meta rich_media_meta_text">金评媒</em>
            <a class="rich_media_meta rich_media_meta_link rich_media_meta_nickname" href="##" id="post-user">i黑马</a>
            <span class="rich_media_meta rich_media_meta_text rich_media_meta_nickname">i黑马</span>
            <div class="profile_inner">
                <strong class="profile_nickname">i黑马</strong>
                <img class="profile_avatar" id="js_profile_qrcode_img" src="/rr?timestamp=1502848075&amp;src=3&amp;ver=1&amp;signature=r6-vL*ZfJdKLh02y9du8x51lDdp0N5cVCnUYhbUYd*uSgkr2Njv0O6NHA0OWAZylxq417ap120AZpxCjq12FzD6ukEJkezg1FCRuQ807ccw=" alt="">

                <p class="profile_meta">
                    <label class="profile_meta_label">微信号</label>
                    <span class="profile_meta_value">kd_express</span>
                </p>
            </div>
        </div>
    </div>
    """

    def _get_detail_p(self, soup):
        result = ()

        head = soup.find('div', id='img-content')
        if head is None:
            print("未读取到标题")
            return

        t_title = head.find('h2', class_='rich_media_title')
        if t_title is not None:
            title = t_title.get_text()
            print(title)

        t_date = head.find('em', id='post-date', class_='rich_media_meta rich_media_meta_text')
        if t_date is not None:
            date = t_date.get_text()
            print(date)

        t_nickname = head.find('span', class_='rich_media_meta rich_media_meta_text rich_media_meta_nickname')
        if t_nickname is not None:
            nickname = t_nickname.get_text()
            print(nickname)

        t_label = head.find('span', class_='profile_meta_value')
        if t_label is not None:
            label = t_label.get_text()
            print(label)

        print('\n')
