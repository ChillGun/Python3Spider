# _*_ coding: utf-8 _*_
from functools import wraps

def log(*msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, ** kw):
            for m in msg:
                if isinstance(m, str) and m != "":
                    print('print: ' + m)
            print('do some decorating')
            return func(*args, **kw)
        return wrapper
    return decorator

@log('有msg参数')
def func1():
    print('func1 is called')

@log()
def func2():
    print('func2 is called')

func1()
func2()