# -*- coding:utf-8 -*-
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2019-9-25')


f = now

f()

print(f.__name__)
