# Python基础

## 数据类型和变量

### 整数

Python可以处理任意大小的整数，包括负整数，如：1，100，-8080，0。
十六进制用0x前缀和0-9，a-f表示，如：0xff00，0xa5b4c3d2。

### 浮点数

浮点数也就是小数（用科学计数法时，小数点位置可变）

数学写法：1.23，3.14，-9.01；

科学计数法：1.23e9，12.3e8，1.2e-5

整数和浮点数在计算机内存储方式不同，整数永远是精确的，浮点数可能有四舍五入的误差。

### 字符串

字符串是以单引号 ' 或双引号 " 括起来的任意文本，如'abc'，"xyz"。

转义字符：\\表示\；\n表示换行；\t表示制表符。

用r''表示''内部的字符串默认不转义，r'\\\t\\' 即表示 \\\t\\

用'''...'''表示多行内容

#### 字符串的编码

ASCII编码，占用一个字节，只包含127个大小写英文、数字和一些符号；

Unicode编码，通常一个字符占用一个字节，生僻字符用4个字节，把所有语言统一到一套编码里面，不会产生乱码问题。

UTF-8编码，“可变长编码”，英文字母一个字节，汉字通常为3个字节，很生僻的字符会编码成4-6个字节。

通用的字符编码工作方式：在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

### 布尔值

Python中用True、False表示布尔值。

布尔值可用and、or和not运算。

### 空值

空值是Python里一个特殊的值，用None表示。

### 变量

Python中变量可以表示任意数据类型

变量名必须是大小写英文、数字和下划线的组合，且不能用数字开头

### 常量

Python中，通常用全部大写的变量名表示常量。

### 列表list

list是一种有序的集合，可以随时添加和删除其中的元素。

如classmates = ['Michael', 'Bob', 'Tracy']

获取某个元素，用下标，如>>>classmates[-1]获取最后一个元素

list末尾增加元素，>>>classmates.append('Adam')

插入元素，>>>classmates.insert(1, 'Jack')

删除末尾元素，>>>classmates.pop()

删除指定位置元素，>>>classmates.pop(i)，其中i是索引位置

### 元组tuple

tuple与list非常类似，但是tuple一旦初始化就不能修改。

如classmates = ('Michael', 'Bob', 'Tracy')

定义空的tuple，t = ()

只有一个元素的tuple，t = (1,)，加一个逗号以区分。

### 字典dict

全称dictionary，使用健-值（key-value）存储，具有极快的查找速度。

与list相比占用内存较多。

定义>>>d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

通过key放入数据：d['Adam'] = 67

删除一个key，>>>d.pop('Bob')

### set

set可以视为一组key的集合，在set中没有重复的key。

重复元素在set中自动被过滤

通过add(key)添加元素到set中

通过remove(key)方法删除元素

### 数据类型转换

## 函数

### 定义函数

```python
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
```

空函数

```python
def nop():
    pass
```

参数检查

```python
def my_abs(x):
    if not ininstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return -x
```

返回多个值

```python
import math

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step.math.sin(angle)
    return nx, ny
```

此时返回值是一个tuple，但在语法上返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值。

```python
>>>x,y = move(100,100,60,math.pi/6)
```

### 函数的参数

#### 位置参数

```python
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

x和n，都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

#### 默认参数

```python
def enroll(name, gender, age=6, city='ChongQing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
```

大多数学生只需提供必须的两个参数

```python
>>>enroll('Sarah','F')
name:Sarah
gender:F
age:6
City:ChongQing
```

只有与默认参数不符的学生才需提供额外信息

```python
enroll('Bob','M',7)
enroll('Adam','M',city="ChengDu")
```

定义默认参数要注意：默认参数必须指向不可变对象！

#### 可变参数

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

```python
>>>calc(1,2)
5
>>>calc()
0
```

也可以把list或tuple前加一个`*`号，把list或tuple的元素变为可变参数

```python
>>>nums = [1,2,3]
>>>calc(*nums)
14
```

#### 关键字参数

关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

```python
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:'kw)
```

使用

```python
>>>person('Adam',45,gender='M',Job='Engineer')
name:Adam age:45 other:{'gender':'M','job':'Engineer'}
```

也可在dict前加**，将dict中所有的key-value用关键字参数传入到函数的kw参数中。

```python
>>>extra = {'city':'ChongQing','job':'Engineer'}
>>>person('jack',24,**extra)
name:Jack age:24 other:{'city':'ChongQing','job':'Engineer'}
```



#### 命名关键字参数

要限制关键字参数的名字，就可以用命名关键字参数，例如，只接受city和job作为关键字参数。定义如下：

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

*后面的参数被视为命名关键字参数。

如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

命名关键字参数必须传入参数名。

命名关键字参数可以有缺省值，从而简化调用：

```python
def person(name, age, *, city='ChongQing', job):
	print(name, age, city, job)
>>>person('jack', 24, job='Engineer')
Jack 24 ChongQing Engineer
```



#### 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但需注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

```python
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args =', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
```

对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

### 递归函数

如果一个函数在内部调用自身，这个函数就是递归函数。

```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
```

使用递归函数需要注意放置栈溢出。

解决递归调用栈溢出的方法时尾递归优化。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。

上面的fact(n)函数有由于return n * fact(n-1)引入了乘法表达式，所以就不是尾递归了。

```python
def fact(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)
```

return fact_iter(num - 1, num * product)仅返回函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。

## 高级特征

### 切片（Slice）

```python
>>>L = list(range(100))
>>>L
[0, 1, 2, 3, ..., 99]
```

前10个数：

```python
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

后10个数：

```python
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

前11-20个数：

```python
>>> L[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

前10个数，每两个取一个：

```python
>>> L[:10:2]
[0, 2, 4, 6, 8]
```

所有数，每5个取一个：

```python
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
```

只写[:]原样复制一个list：

```python
>>> L[:]
>>>[0, 1, 2, 3, ..., 99]
```

字符串也可以用切片功能：

```python
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'
```

### 迭代（Iteration）

通过for循环来遍历可迭代对象，这种遍历称为迭代（Iteration）。

只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

```python
>>> d = {'a':1, 'b':2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
b
c
```

默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

字符串也是可迭代对象，可用for循环：

```python
>>> for ch in 'abc':
...     print(ch)
...
a
b
c
```

判断一个对象是否是可迭代对象，可以通过collections模块的Iterable类型判断：

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) #可迭代
True
>>> isinstance([1,2,3], Iterable) #可迭代
True
>>> isinstance(123, Iterable) #不可迭代
False
```

Python的enumerate函数可以把一个list变成索引元素对，这样在for循环中就可以同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['a', 'b', 'c']):
...     print(i,value)
...
0 a
1 b
2 c
```

### 列表生成式（List Comprehensions  ）

要生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用 list(range(1, 11))：

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

生成[1x1, 2x2, 3x3, ..., 10x10]，使用循环：

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

使用列表生成式：

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

可以在式子中加上if判断，仅筛选出偶数的平方：

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

使用两层循环，可以生成全排列：

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

使用列表生成式，列出当前目录下所有文件：

```python
>>> import os
>>> [d for d in os.listdir('.')]
```

### 生成器

在python中一边循环一边计算的机制，称为生成器：generator

将列表生成器中的[]改为()，就创建了一个generator：

```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x000001DC0F94F900>
```

通过next()函数获得generator的下一个返回值：

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
...
>>> next(g)
81
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

使用for循环迭代generator对象：

```python
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
...
0
1
4
9
16
25
36
49
64
81
```

斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1，2，3，5，8，13，21，34，...

斐波拉契数列用列表生成式写不出来，但是，用函数打印出来却很容易：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
```

此函数可以推算出斐波拉契数列的任意前N个数：

```python
>>> fib(6)
1
1
2
3
5
8
'done'
```

将以上函数中的print(b)改为yield b，就把fib函数变成了generator：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

关于yield的说明：调用有yield的函数时，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

使用for循环来迭代上述函数：

```python
>>> for n in fib(6):
...     print(n)
...
1
1
2
3
5
8
```

如果要拿return语句中的值，需捕获StopIteration错误，返回值包含在StopIteration的value中：

```python
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
```

### 迭代器

可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

```python
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：

```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str、等Iterable变成Iterator可以使用iter()函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

## 函数式编程

### 高阶函数

##### 变量可以指向函数

```python
>>> f = abs
>>> f
<built-in function abs>
>>> f(-10)
10
```

变量指向函数后，可直接通过变量来调用函数。

##### 函数名也是变量

对于abs()这个函数，可把abs看成是变量，它指向一个可以计算绝对值的函数。

```python
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

可将其它值赋给abs，abs就指向了其它值。

##### 传入函数

变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另外一个函数作为参数，这种函数就称为高阶函数。

一个简单的高阶函数：

```python
def add(x, y, f):
    return f(x) + f(y)
```

当调用add(-5, 6, abs)时，参数x, y和f分别接收-5，6和abs，根据函数定义，可推导计算过程为：

```python
x = -5
y = 6
f = abs
f(x) + f(y) ==>abs(-5) + abs(6) ==> 11
```

验证计算结果

```python
>>> add(-5,6,abs)
11
```

#### map/reduce

map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

将函数f(x)=x^2，作用在一个list[1, 2, 3, 4, 5, 6 ,7 ,8, 9]上，用map()实现如下：

```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7 ,8 ,9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

将一个list中的所用数字转为字符串：

```python
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

reduce的用法，reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果：

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

使用`reduce`将序列`[1, 3, 5, 7, 9]`变换成整数`13579`：

```python
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```

利用map和reduce实现一个str转换为int的函数：

```python
from functools import reduce

DIGITS = {'0': 0, '1':1, '2':2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGIts[S]
    return reduce(fn, map(char2num, s))
```

使用示例1

```python
# _*_ coding: utf-8 _*_

# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart'].

def normalize(name):
    return name[0].upper()+name[1:].lower()

# 测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
```

使用示例2

```python
# _*_ coding utf-8 _*_

# 使用map和reduce函数将字符串转化为浮点数

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    
    # 将字符串以小数点为界分为两个字符串
    dotpla = s.index('.')
    L1 = s[:dotpla]
    L2 = s[dotpla+1:]

    # 将两个字符串转为int
    # 第一个字符串转换过来即可
    # 第二个字符串需除以自身的长度以确定小数点的位置
    L1_ = reduce(fn, map(char2num, L1))
    L2_ = (reduce(fn, map(char2num, L2))/(10**len(L2)))

    return L1_ + L2_
    
```



#### filter

Python内建的filter()函数用于过滤序列。

filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

例如，在一个list中，删除偶数，只保留奇数，可以如下实现：

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果：[1, 5, 9, 15]
```

注意到`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list。

回数是指从左向右读和从右向左读都是一样的数，使用filter()筛选出回数：

```python
# -*- coding: utf-8 -*-

def is_palindrome(n):
    # 此处使用切片进行处理，非常精妙
    return int(str(n)[::-1]) == n

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
```

#### sorted

Python内置的sorted()函数就可以对list进行排序：

```python
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

`sorted()`函数是一个高阶函数，它还可以接收一个`key`函数实现自定义排序：

```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

对字符串排序，忽略大小写：

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

反向排序，传入第三个参数`reverse=True`：

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

示例：

```python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)

#按成绩从高到低排序：
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)
```

### 返回函数

#### 函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

如下函数返回的是一个求和函数：

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```

调用`lazy_sum`时，返回的并不是求和结果，二十求和函数：

```python
>>>f = lazy_sum(1, 3, 5, 7, 9)
>>>f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
```

调用函数`f`时，才返回计算求和的结果：

```python
>>>f()
25
```

#### 闭包

上面的例子中，在函数`lazy_sum`中定义了`sum`，并且，内部函数`sum`引用了外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在返回的函数中，这种程序结构成为“闭包（Closure）”。

需要注意的是，返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如下函数，连续调用时会返回同样的值

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

>>> f1()
9
>>> f2()
9
>>> f3()
9
```

原因在于返回的函数引用了变量`i`，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量`i`已经变成了`3`，因此最终结果为`9`。

修改如下：

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)被立刻执行，因此i的当前值被传入f()
    return fs
```

结果如下：

```python
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```

例子：

利用闭包返回一个计数器函数，每次调用它返回递增整数：

```python
# def createCounter():
#     a = [0]
#     def counter():
#         a.append(len(a))
#         return a[-1]
#     return counter

# def createCounter():
#     L=[0]   #初始化列表L只有一个元素0
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
```

#### 匿名函数

关键字`lambda`表示匿名函数，冒号前面表示函数参数。

```python
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

可以看出，匿名函数`lambda x: x * x`实际上就是：

```python
def f(x):
    return x*x
```

也可把匿名函数作为返回值使用，比如：

```python
def build(x, y):
    return lambda: x * x + y * y
```

#### 装饰器

在代码运行期间动态增加功能的方式，称为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。

定义一个能打印日志的decorator，可定义如下：

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

上面的`log`接受一个函数作为参数，并返回一个函数。使用装饰器时，借助python的@语法，把decorator置于函数的定义处：

```python
@log
def now():
    print('2021-10-12')
```

调用`now()`函数，不仅会运行`now()`函数本身，还会在运行`now()`函数前打印一行日志：

```python
>>>now()
call now():
2021-10-12
```

把`@log`放在`now()`函数的定义处，相当于执行了语句：

```python
now = log(now)
```

如下定义一个需要传入参数的decorator：

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decoraotor
```

这个3层嵌套的decorator用法如下：

```python
@log('execute')
def now():
    print('2021-10-12')
```

执行结果如下：

```python
>>>now()
execute now():
2021-10-12
```

3层嵌套的效果如下：

```python
>>>now = log('execute')(now)
```

Python内置的`functools.wraps()`可实现`wrapper.__name__ = func.__name__`的效果，保证有些依赖数字签名的代码正确执行，如下：

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

或者针对带参数的decorator：

```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

例子

```python
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
```

同时实现可传入参数和不可传入参数

```python
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
```

#### 偏函数

`functools.partial`的作用是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新函数，调用这个新函数会更简单。

定义一个转换二进制字符串的函数：

```python
def int2(x, base=2):
    return int(x, base)
```

使用`functool.partial`可以直接使用下面的代码创建一个新的函数`int2`：

```python
>>>import functools
>>>int2 = functools.partial(int, base=2)
>>>int2('1000000')
64
>>>int2('1010101')
85
```

创建偏函数时，实际上可以接收函数对象、`*args`和`**kw`这三个参数，

```python
int2 = functools.partial(int, base=2)
int2('10010')
```

相当于：

```python
kw = {base: 2}
int('10010',**kw)
```

区分

```python
max2 = functools.partial(max, 10)
max2(5, 6, 7)
```

相当于

```python
args = (10, 5, 6, 7)
max(*args)
```

结果为`10`。

## 模块

为了编写可维护的代码，我们把很多函数分组，分别放在不同的文件里，这样，每个文件包含的代码就相对较少，，很多编程语言都采用这种组织代码的方式。在Python中，一个`.py`文件就称之为一个模块（Module）。

使用模块的好处：

1、提高代码的可维护性。

2、避免函数名和变量名冲突。

为了避免模块名的冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。

引入了包以后，只要顶层的包名不与别人冲突，那所用的模块都不会与别人冲突。如`mycompany`包下面有`abc.py`模块，那`abc.py`的名字就变成了`mycompany.abc`。

需要注意，每个包目录下面都有一个`__init__.py`的文件，这个文件表示该目标表示一个包（Package），没有该文件则表示一个普通目录。`__init__.py`可以是空文件，也可以是Python代码，因为`__init__.py`本身就是一个模块，它的模块名与包名相同。

### 使用模块

以`sys`模块为例，编写一个`hello`模块：

```python
#！/usr/bin/enw python
# -*- coding: utf-8 -*-

'a test module'

__author__='Michael Liao'

import sys

def test():
    args = sys.argv # argv变量，用list存储了命令行的所有参数。
    if len(args)==1:
        print 'hello, world!'
    elif len(args)==2:
        print 'Hello, %s' % srgs[1]
    else:
        print 'Too may arguments!'

if __name__=='__main__':
    test()
```

第一行注释让这个`hello.py`文件可直接在Unix/Linux/Mac上运行；

第二行表示该文件本身使用UTF-8编码；

第四行是一个字符串，表示模块的文档注释；

`__author__`变量表示作者

```python
import sys
```

表示导入`sys`模块，导入该模块就有了变量`sys`指向该模块，以用`sys`这个变量，就可以访问`sys`模块的全部功能。

注意最后两行代码：

```python
if __name__=='__main__':
    test()
```

当在命令行运行`hello`模块文件时，Python解释器把一个特殊变量`__name__`置为`__main__`，而在其它地方导入该`hello`模块时，`if`判断将失败，因此，这种`if`测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

#### 别名

导入模块时，使用别名，可以在运行时根据当前环境选择最合适的模块。

`StringIO`和`cStringIO`，这两个库的接口和功能是一样的，但有些平台不支持`cStringIO`，为提高代码通用性，可如下实现：

```python
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
```

`simplejson`库，在Python2.6之前是独立的第三方库，从2.6开始内置，可以这样写：

```python
try:
    import json #python >= 2.6
except ImportError:
    import simplejson as json #python <= 2.5
```

#### 作用域

正常的函数和变量名是公开的（public），可以被直接引用。

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的`__author__`，`__name__`就是特殊变量，自己定义变量时不要使用这种变量。

类似`_xxx`和`__xxx`这样的函数或者变量时非公开的（private），不应该被直接引用，但是Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

## 面向对象编程

面向对象编程——Object Oriented Programming，简称OOP，是一种程系设计思想。

面向过程的程序设计把计算机程序视为一些列命令的集合，即一组函数顺序执行。为了简化程序设计，面向过程继续把函数切分为子函数，即把大块函数通过切割成小块函数来降低系统复杂度。

面向对象的程序设计把计算机程序视为一组对象的集合，每个对象都可以接收其它对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间的传递。

### 类和实例

类（Class）是抽象的模板，比如Student类；

实例（Instance）是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

类的定义通过关键字`class`实现：

```python
class Student(object):
    pass
```

`class`后面紧接着类名，即`student`，类名通常用大写字母开头，紧接着括号内表示该类从哪个类继承而来，所有的类都会继承`object`类。

定义类的时候，通过定义一个特殊的`__init__`方法，在创建实例的时候，把所需的属性绑定上去。

```python
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

有了`__init__`方法，在创建实例的时候，就需要传入相应的参数了，其中`self`不用传，Python解释器会自己把实例变量传进去。

```python
>>>bart = Student('Bart Simpson', 59)
>>>bart.name
'Bart Simpson'
>>>bart.score
59
```

#### 数据封装

面向对象编程的一个种要特点就是数据封装。

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print '%s: %s' % (self.name, self,score)
```

```python
>>>bart.print_score()
Bart Simpson: 59
```

利用如上类创建实例只需要给出`name`和`score`，而如何打印，都在`Student`类的内部定义好了，这些数据和逻辑都被“封装”起来了，调用很容易，但却不知道内部实现的细节。

封装的另外一个好处是可以给`Student`类增加新的方法，比如`get_grade`：

```python
class Student(object):
    ...
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
```

```python
>>>bart.get_grade()
'C'
```

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，
互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现
细节。

和静态语言不同，Python 允许对实例变量绑定任何数据。

### 访问限制

Python中，在属性变量名前加两个下划线`__`，就表示该变量变成了一个私有变量（private），只有内部可以访问，外部不能访问。

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
```

为了从外部获取name和score，可以给Student类增加`get_name`和`get_score`这样的方法：

```python
class Student(object):
    ...
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
```

要从外部修改score，可以给Student类增加`set_score`方法：

```python
class Student(object):
    ...
    
    def set_score(self, score):
        self.__score = score
```

还可以在方法中，对传入的参数进行检查：

```python
class Student(object):
    ...
    
    def set_score(self, score):
        if 0 <= score <=100:
            self.__score = score
        else：
        	raise ValueError('bad score')
```

Python实现私有变量是通过解释器把带双下划线的变量名改成其它变量名实现的。

### 继承和多态

在OOP程序设计中，当我们定义一个class的时候，可以冲某个现有的calss继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

子类可获得全部功能。

子类和父类都存在相同的方法时，子类的方法会覆盖父类的方法，运行代码时，总是会调用子类的方法。这就是继承的另一个好处：多态。

### 获取对象信息

#### 使用type()

基本类型都可以用`type()`判断对象类型：

```python
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<class 'NoneType'>
```

如果一个变量指向函数或者类，也可以用`type()`判断：

```python
>>> type(abs)
<class 'builtin_function_or_method'>
```

Python把每种type定义好了常量，放在`types`模块里，使用之前，需要先导入：

```python
>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True
```

#### 使用isinstance()

```python
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True
```

#### 使用dir()

`dir()`函数可获得一个对象的所有属性和方法，返回一个包含字符串的list。

```python
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

类似`__xxx__`的属性和方法在python中都是有特殊用途的，比如`__len__`方法返回长度，在Python中，如果调用`len()`函数试图获取一个对象的长度，实际上，在`len()`函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```



## 面向对象高级编程

### 使用`__slots__`

`__slots__`的作用是限制class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义运行绑定的属性名称
```

使用

```python
>>>s = Student() #创建新的实例
>>>s.name = 'Michael' #绑定属性‘name’
>>>s.age = '25' #绑定属性‘age’
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

`__slots__`定义的属性仅对当前类实例起作用，对继承的子类不起作用。

除非子类中也定义`__slots__`，这样，子类实例运行定义的属性就是自生的`__slots__`加上父类的`__slots__`。

### 使用@property

Python内置的`@property`装饰器负责把一个方法变成属性调用：

```python
class Student(object):
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
```

`@property`把一个getter方法变成了属性，同时，`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个setter方法百年城属性赋值。

```python
>>>s = Student()
>>>s.score = 60 # OK，实际转化为s.set_score(60)
>>>s.score # OK，实际转化为s.get_score()
60
>>>s.score = 90
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```

需要注意：属性的方法名不要和实例变量重名。注意上面的`score`和`_score`的区分。

### 多重继承

定义哺乳类和鸟类

```python
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Amimal):
    pass
```

定义`Runnable`和`Flyable`类：

```python
class Runnable(object):
    def run(self):
        print('Running...')
        
class Flyable(object):
    def fly(self):
        print('Flying...')
```

定义一个`Runnable`的哺乳动物，例如`Dog`:

```python
class Dog(Mammal, Runnable):
    pass
```

定义一个`Flyable`的哺乳动物，例如`Bat`：

```python
class Bat(Mammal, Flyable):
    pass
```

#### Mixin

在设计继承关系时，如果要“混入”额外的功能，通过多重继承就可以实现。这种设计同城称之为Mixin

为了更好地看出继承关系，把`Runnable`和`Flyable`改为`RunnableMixin`和`FlyableMixin`。还可以定义肉食动物`CarnivorousMixin`和植食动物`HerbivoresMixin`，让某个动物同时拥有好几个Mixin：

```python
class Dog(Mammal, RunnableMixin, CarnovorousMixin):
    pass
```

  在设计类的时候，优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。

例如，一个多进程模式的TCP服务：

```python
class MyTCPServer(TCPServer, ForkingMixin):
    pass
```

一个多进程的UPD服务：

```python
class MyUDPServer(UDPServer, ThreadingMixin):
    pass
```

只允许单一继承的语言（如Java）不能使用Mixin的设计。

### 定制类

类似`__slots__`这种形如`__xxx__`的变量或者函数名就要注意，这些在Python中有特殊用途的。

#### `__str__`

定义好`__str__()`方法，返回一个好看的字符串：

```python
>>> class Student(object):
... def __init__(self, name):
... self.name = name
... def __str__(self):
... return 'Student object (name: %s)' % self.name
...
>>> print Student('Michael')
Student object (name: Michael)
```

`__repr__()`返回程序开发者看到的字符串。可以如下写：

```python
__repr__ = __str__
```



#### `__iter__`

如果一个类想被用于`for...in`循环，类似list和tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`next()`方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

以斐波那契数列为例，写一个Fib类，可以作用域for循环：

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a, b
        
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def next(self):
        self.a, self.b = self.b, self.a + self.b 
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
```

现在，试试吧Fib实例作用于for循环：

```python
>>> for n in Fib():
... print n
...
1
1
2
3
5
...
46368
75025
```

#### `__getitem__`

定义一个类，使其表现得像list那样能获取元素和切片，需要实现`__getitem__()`方法：

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L =  []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```

上述定义还没有对负数做处理，所以，要正确实现一个`__getitem__()`还要许多工作要做。

#### `__getattr__`

定义`__getattr__`可以把一个类的所有属性和方法调用全部动态化处理，不需要任何特殊手段。

可以针对完全动态的情况做调用。

比如：

现在很多网站都高REST API，比如新浪微博、豆瓣...，调用的API的URL类似：

```apl
http://api.server/user/friends
http://api.server/user/timeline/list
```

如果要写SDK，给每个URL对应的API都写一个方法，工作繁杂重复，而且，API一旦改动，SDK也要改。

利用完全动态的`__getattr__`，我们可以写出一个链式调用：

```python
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    
    def __str__(self):
        return self._path
    
    __repr__=__str__
```

使用结果如下：

```python
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

#### `__call__`

在类中定义一个`__call__()`方法，可实现直接在实例本身上调用`__call__()`中定义的内容，类似`instance()`。

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('My name is %s.' % self.name)
```

调用方式如下：

```python
>>>s = Student('Michael')
>>>s()
My name is Michael.
```

`__call__()`还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以完全可以把对象看成函数，把函数看成对象。

要判断一个对象是否是“可调用”对象，可以使用`callable()`函数。

```python
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
```

### 使用枚举类



### 使用元类













