# _*_ coding utf-8 _*_
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):

    dotpla = s.index('.')

    def fn(x,y):
        return x*10 + y

    def char2num(s):
        return DIGITS[s]
    
    L1 = s[:dotpla]
    L2 = s[dotpla+1:]

    L1_ = reduce(fn, map(char2num, L1))
    L2_ = (reduce(fn, map(char2num, L2))/(10**len(L2)))

    return L1_ + L2_
    

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
        

