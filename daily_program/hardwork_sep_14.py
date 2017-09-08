# -*- coding:utf-8 -*-


class HardWork:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def format_str(self):
        # 使用format()方便字符串处理
        print("{0} is {1} years old when he wrote this book".format(self.name, self.age))
        print("{} is {} years old when he wrote this book".format(self.name, self.age))
        print("{1} is {0} years old when he wrote this book".format(self.name, self.age))
        print('Why {0} playing with that python?'.format(self.name))

        # 对于浮点数 '0.333' 保留小数点(.)后三位
        print('{0:.3f}'.format(1 / 3))

        # 使用下划线填充文本，并保持文字处于中间位置
        # 使用 (^) 定义 '___hello___'字符串长度为 11
        print('{0:_^11}'.format('hello'))

        # 基于关键词输出 'Swaroop wrote A Byte of Python'
        print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

        # print总是会以一个不可见的“新一行”字符（\n）结尾
        print('a', end='')
        print('b', end='_')
        print('c')

    def birthday(self, age):
        print(self.name, age)
        return 2017 - age


hard = HardWork('Tom', 26)
hard.format_str()
ages = [22, 21, 26]
print(list(map(hard.birthday, ages)))
print(list(map(str, ages)))
