#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType


class Student(object):

    def __str__(self):
        return 'Student object (name: %s)' % '我勒个去'
    __repr__ = __str__


class Money(object):
    # 为了限制实例的属性
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('color', 'value', '_score')

    # 检查参数限制范围,又可以用类似属性这样简单的方式来访问类的变量
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


def set_age(self, age):
    self.age = age


if __name__ == '__main__':
    s = Student()
    s.name = 'Michael'
    print(s.name)

    # 给实例绑定一个方法
    s.set_age = MethodType(set_age, s)
    s.set_age(23)
    print(s.age)

    # 给一个实例绑定的方法，对另一个实例是不起作用的
    s2 = Student()
    # s2.set_age(22)
    print(s2)
    s2

    # 为了给所有实例都绑定方法，可以给class绑定方法：
    Student.set_age = set_age
    s2.set_age(22)
    print(s2.age)

    m = Money()
    m.color = 'red'
    m.value = 100
    m.score = 80
    print(m.score)

    sce = Screen()
    sce.height = 1024
    sce.width = 768
    print(sce.resolution)
    assert sce.resolution == 786432, '1024 * 768 = %d ?' % sce.resolution

