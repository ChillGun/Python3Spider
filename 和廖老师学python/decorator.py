# _*_ coding: utf-8 _*_
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')

#分析一下过程，执行
# f = fast(11, 22)
#相当于执行
# 首先执行 metric(fast(x, y))
# 返回 wrapper 函数
# 调用 wrapper 函数执行打印语句然后 返回 fn 函数
# 最后再执行 