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

也可以把list或tuple前加一个*号，把list或tuple的元素变为可变参数

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