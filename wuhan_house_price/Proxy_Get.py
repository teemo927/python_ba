#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
from urllib import request

import time
from bs4 import BeautifulSoup


class Proxy_Get(object):
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 "
            "Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 "
            "Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 "
            "Safari/535.24 "
        ]
        self.ip_list = self.get()

    def get(self):
        p_lists = []
        url = 'http://www.xicidaili.com/nn/'
        u_a = random.choice(self.user_agent_list)
        head = {'User-Agent': u_a}
        req = request.Request(url, headers=head)
        response = request.urlopen(req)
        result = response.read()
        soup = BeautifulSoup(result, 'html.parser')

        # <table id="ip_list">
        tr_lists = soup.find('table', id='ip_list').findAll('tr')
        for tr in tr_lists:
            td_lists = tr.findAll('td')
            if td_lists is not None and len(td_lists) > 3:
                p_lists.append(td_lists[1].get_text() + ":" + td_lists[2].get_text())

        print(p_lists)
        print(len(p_lists))
        return p_lists

    def proxy_url(self, url):
        u_a = random.choice(self.user_agent_list)
        head = [('User-Agent', u_a)]
        i_p = str(random.choice(self.ip_list)).strip()  # 下面有解释哦
        print('\nu_a:', u_a, "\nproxy_ip:", i_p)
        # # 这是代理IP
        proxy = {'http': i_p}
        # 创建ProxyHandler
        proxy_support = request.ProxyHandler(proxy)
        # 创建Opener
        opener = request.build_opener(proxy_support)
        # 添加User Angent
        opener.addheaders = head
        # 安装OPener
        request.install_opener(opener)
        try:
            # 计时开始
            begin = time.time()
            # 使用自己安装好的Opener
            response = request.urlopen(url, timeout=5)
            speed = round(time.time() - begin, 2)
            print(speed)
            # 读取相应信息并解码
            html = response.read()
            return html
        except Exception as e:
            print(e)
            return self.proxy_url(url)


if __name__ == '__main__':
    p = Proxy_Get()
    start = 'http://scxx.whfcj.gov.cn/xmqk.asp?page=1'
    # start = 'http://www.baidu.com'
    res = p.proxy_url(start)
    print(res)
