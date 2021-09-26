# -*- coding: utf-8 -*-


# def createCounter():
#     a = [0]
#     def counter():
#         a.append(len(a))
#         return a[-1]
#     return counter

# def createCounter():
#     L=[0]   #初始化列表L为0
#     def counter():
#         L[0]+=1     #L[0]指的是列表L的第一个元素，为一个可变变量
#         return L[0]
#     return counter

# def createCounter():
#     x=0
#     def counter():
#         nonlocal x
#         x=x+1
#         return x
#     return counter
    #利用nonlocal关键字声明变量x，
    # 既不是局部变量，也不是全局变量，
    # 需要向上一层变量空间找这个变量。
    # 只在闭包里面生效，只能用在嵌套函数中，
    # 是python3中新添的关键字，python2中无。
    # 作用理解是：x保存内函数counter每次作用后返回的值，
    # 比如第一次x=0，counter()后，x=0+1=1，counter（）后，x=1+1=2......以此类推

def createCounter():
    def g():    #生成器生成有序数列1，2，3......
        n=0
        while 1:
            n+=1
            yield n
    a=g()
    def counter():
        return next(a)  #每次调用next()函数获得生成器的下一个返回值
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
