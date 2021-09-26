#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kw):
        print('before called')
        func()
        print('after callded')
    return wrapper


@decorator
def myfunc():
    print('this func is called')


myfunc()