#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


def log(text='Start call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            f = func(*args, **kw)
            print('End call: %s' % func.__name__)
            return f

        return wrapper

    return decorator


@log('wo ca ca')
def now():
    print('呵呵')


@log()
def now2():
    print('啥都不说了')


now()
print(now.__name__, '\n')
now2()
