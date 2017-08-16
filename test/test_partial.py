#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import types


def do():
    test = functools.partial(int, base=2)
    print(test('1010'))
    print(test('1010', base=4))

    max2 = functools.partial(max, 10)
    print(max2(22))


class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')


class Pig(Animal):
    pass


class People(object):
    name = '中国人'

    def run(self):
        print('people is running')


def run_twice(animal):
    animal.run()
    animal.run()


def test_type():
    print(type(run_twice) == types.FunctionType)
    pass


'''
Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''


def test_name():
    s = People()
    print(s.name)
    print(People.name)
    s.name = '阿三'
    print(s.name)
    print(People.name)
    del s.name
    print(s.name)


if __name__ == '__main__':
    do()
    run_twice(Animal())
    run_twice(Dog())
    '''
    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    Python的“file-like object“就是一种鸭子类型
    '''
    run_twice(People())
    test_type()

    test_name()
