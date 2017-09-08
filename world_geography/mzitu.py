import os
from urllib import request

from PIL import Image
from bs4 import BeautifulSoup

from Base_Downloader import downloader


class mzitu():
    def all_url(self, url):

        html = downloader.get(url)
        all_a = BeautifulSoup(html.read(), 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)
            os.chdir("D:\mzitu\\" + path)
            href = a['href']
            self.html(href)

    def html(self, href):
        html = downloader.get(href)
        max_span = BeautifulSoup(html.read(), 'lxml').find_all('span')[10].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self, page_url):
        img_html = downloader.get(page_url)
        img_url = BeautifulSoup(img_html.read(), 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = downloader.get(img_url)
        f = open(name + '.jpg', 'wb')
        f.write(img.read())
        f.flush()
        f.close()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False


if __name__ == '__main__':
    Mzitu = mzitu()  # 实例化
    Mzitu.all_url('http://www.mzitu.com/all')  # 给函数all_url传入参数  你可以当作启动爬虫（就是入口）
