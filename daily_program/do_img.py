#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import random
import string

from PIL import Image, ImageSequence, ImageDraw, ImageFilter, ImageFont

"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""


class DoImg(object):
    pass


# 使用系统浏览器打开GIF
def open_gif():
    os.system(r'F:/py/python_ba/download_img/py_downloads/b.gif')


# 翻转gif
def reverse_gif():
    # img = Image.open('py_downloads/c.gif')
    with Image.open('F:\py\python_ba\download_img\py_downloads\car.gif') as img:
        if img.is_animated:
            frames = [f.copy() for f in ImageSequence.Iterator(img)]
            frames.reverse()  # 倒序
            frames[0].save('py_downloads/car_back.gif', save_all=True, append_images=frames[1:])


# 遍历文件夹
def open_all(path):
    # '*'代表匹配所有文件
    files = glob.glob(path + os.sep + '*')
    for f in files:
        if os.path.isdir(f):
            open_all(f)
        else:
            print(f)


# 遍历失败
def open_all_failed(path):
    for f in os.listdir(path):
        if os.path.isdir(f):
            open_all_failed(f)
        else:
            print(f)


def img_g():
    im = Image.open(r'F:\py\python_ba\download_img\py_downloads\psb.jpg')

    im = im.convert("L")  # 转换为灰度图像
    im.save(r'F:\py\python_ba\download_img\py_downloads\psb_gray.jpg')
    im = im.filter(ImageFilter.EDGE_ENHANCE)  # 基本滤波之 边缘增强
    im.save(r'F:\py\python_ba\download_img\py_downloads\psb_pro.jpg')


# 给图片加水印
def img_do():
    location = r'F:\py\python_ba\daily_program\file\a.jpg'
    img = Image.open(location)

    # 获得当前图片的大小，根据此参数设置字体大小
    xSize, ySize = img.size
    ttfont = ImageFont.truetype(r'F:\py\python_ba\daily_program\file\mei.ttf', int(ySize / 8))

    draw = ImageDraw.Draw(img)
    # 在图片上直线
    draw.line((0, 0) + img.size, fill=128, width=20)
    draw.line((0, ySize, xSize, 0), fill=(0, 200, 0), width=10)

    # 在图片上添加字符QQ2134567890
    draw.text((xSize * 0.2, 0), 'QQ2134567890', fill=(255, 0, 0), font=ttfont)

    # 在图片上添加弧线
    # 画圆
    draw.ellipse((150, 150, 350, 350), outline=128)
    draw.chord((0, 0, 500, 500), 0, 270, outline='red')
    del draw

    img.show()
    # 根据输入的命名来设置新图片名字，默认设置为“原名_new”，格式与原图相同
    img.save(location.split('.')[0] + '_new.' + location.split('.')[-1])


def create_code(len1, start_str=''):
    elements = string.digits + string.ascii_letters
    r = random.choice(elements)
    result = start_str + str(r)
    if len(result) < len1:
        return create_code(len1, result)
    else:
        print('result:', result)
        return result


# ---------------------------------------
# 功能：输入生成激活码的数量和长度后，会产生对应数字的激活码，并保存在当前目录下
# ---------------------------------------
def img_random(text, addr):
    ttfont = ImageFont.truetype(r'F:\py\python_ba\daily_program\file\mei.ttf', 32)
    # if text is not None:
    img = Image.new('RGB', size=(200, 150), color='gray')
    draw = ImageDraw.Draw(img)
    draw.text((20, img.size[1] / 2), text, fill=(255, 0, 0), font=ttfont)
    draw.line((20, img.size[1] / 2 + 15, img.size[0], img.size[1] / 2 + 15), fill='purple')
    draw.line((20, img.size[1] / 2 + 30, img.size[0], img.size[1] / 2 + 10), fill='black')
    img.show()
    img.save(addr + text + '.jpg')


# 生成随机验证码，并输出图片
def create_codes():
    # 设置激活码存放文件名，设置每位激活码的取值域
    file_address = 'file/codes/'
    if not os.path.exists(file_address):
        os.mkdir(file_address)

    number = input("Please input the number of keys:")
    length = input("Please input the length of keys:")
    length = 8 if int(length) > 8 else length
    codes = []
    for i in range(int(number)):
        result = create_code(int(length))
        codes.append(result)
        img_random(result, file_address)
    print(codes)


if __name__ == '__main__':
    # open_gif()
    # reverse_gif()

    # open_all(r'E:\买买买\buy')
    # open_all_failed(r'E:\买买买\buy')

    # img_g()
    # img_do()
    create_codes()
