#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import re
import time
from urllib import request

from bs4 import BeautifulSoup


class BaseDownloader:
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
        self.iplist = self.p_list()

    def p_list(self):
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
        return p_lists

    def get(self, url, proxy=None, num_retries=0):
        u_a = random.choice(self.user_agent_list)
        head = {'User-Agent': u_a}
        req = request.Request(url, headers=head)
        if proxy is None:
            # try:
            #     return request.urlopen(req)
            # except:  # 如过上面的代码执行报错则执行下面的代码
            #     print('error!!11')
            if num_retries > 0:  # num_retries是我们限定的重试次数
                time.sleep(10)  # 延迟十秒
                print(u'获取网页出错，10S后将获取倒数第：', num_retries, u'次')
                return self.get(url, num_retries=num_retries - 1)  # 调用自身 并将次数减1
            else:
                print(u'开始使用代理')
                # time.sleep(10)
                i_p = str(random.choice(self.iplist)).strip()  # 下面有解释哦
                # # 这是代理IP
                proxy = {'http': i_p}
                # 创建ProxyHandler
                proxy_support = request.ProxyHandler(proxy)
                # 创建Opener
                opener = request.build_opener(proxy_support)
                # 安装OPener
                request.install_opener(opener)
                return request.urlopen(req)
        else:
            try:
                # 将从self.iplist中获取的字符串处理成我们需要的格式（处理了些什么自己看哦，这是基础呢）
                i_p = str(random.choice(self.iplist)).strip()
                proxy = {'http': i_p}  # 构造成一个代理
                # 创建ProxyHandler
                proxy_support = request.ProxyHandler(proxy)
                # 创建Opener
                opener = request.build_opener(proxy_support)
                # 安装OPener
                request.install_opener(opener)
                return request.urlopen(req)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    i_p = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': i_p}
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.get(url, proxy, num_retries - 1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.get(url, 3)

    def ip_list(self):
        ip_lists = []  # 初始化一个list用来存放我们获取到的IP
        html = self.get("http://haoip.cc/tiqu.htm")  ##不解释咯
        # soup = BeautifulSoup(response, 'html.parser')

        ip_list = re.findall(r'r/>(.*?)<b', html.text,
                             re.S)  # 表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
        for ip in ip_list:
            i = re.sub('\n', '', ip)  # re.sub 是re模块替换的方法，这儿表示将\n替换为空
            ip_lists.append(i.strip())  # 添加到我们上面初始化的list里面, i.strip()的意思是去掉字符串的空格哦！！（这都不知道的小哥儿基础不牢啊）
            print(i.strip())
        print(ip_lists)


if __name__ == '__main__':
    downloader = BaseDownloader()
    # start = 'http://www.mzitu.com/'
    start = 'http://www.baidu.com/'
    res = downloader.get(start)
    print(res.read())
