'''
6 字典推导式

可能你见过列表推导时,却没有见过字典推导式,在2.7中才加入的:

d = {key: value for (key, value) in iterable}

name = ["张三", "李四", "王五", "李六"]  # 保存名字列表
sign = ["白羊座", "双鱼座", "狮子座", "处女座"]  #保存星座列表
dict1 = {i : j for i, j in zip(name, sign)}    # 字典推导式
print(dict1)

{'张三': '白羊座', '李四': '双鱼座', '王五': '狮子座', '李六': '处女座'}
'''


'''

7 Python中单下划线和双下划线

class MyClass():

    def __init__(self):

        self.__superprivate = "Hello"

        self._semiprivate = ", world!"

...

mc = MyClass()

print mc.__superprivate

Traceback (most recent call last):

  File "", line 1, in

AttributeError: myClass instance has no attribute '__superprivate'

print mc._semiprivate

, world!

print mc.__dict__

{'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}

__foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突，就是例如__init__(),__del__(),__call__()这些特殊方法

_foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.不能用from module import * 导入，其他方面和公有一样访问；

__foo:这个有真正的意义:解析器用_classname__foo来代替这个名字,以区别和其他类相同的命名,它无法直接像公有成员一样随便访问,通过对象名._类名__xxx这样的方式可以访问.

'''


'''
8 字符串格式化:%和.format

.format在许多方面看起来更便利.对于%最烦人的是它无法同时传递一个变量和元组.你可能会想下面的代码不会有什么问题:

"hi there %s" % name

但是,如果name恰好是(1,2,3),它将会抛出一个TypeError异常.为了保证它总是正确的,你必须这样做:

"hi there %s" % (name,)   # 提供一个单元素的数组而不是一个参数

但是有点丑..format就没有这些问题.你给的第二个问题也是这样,.format好看多了.

你为什么不用它?

不知道它(在读这个之前)
为了和Python2.5兼容(譬如logging库建议使用%(issue #4))
'''

'''

9 迭代器和生成器


这里有个关于生成器的创建问题面试官有考：
问： 将列表生成式中[]改成() 之后数据结构是否改变？
答案：是，从列表变为生成器

L = [x*x for x in range(10)]

L

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x*x for x in range(10))

g

at 0x0000028F8B774200>

通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator
'''

'''
10 *args and **kwargs

用*args和**kwargs只是为了方便并没有强制使用它们.

当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:

def print_everything(*args):

    for count, thing in enumerate(args):

        print '{0}. {1}'.format(count, thing)



print_everything('apple', 'banana', 'cabbage')

0. apple

1. banana

2. cabbage

相似的,**kwargs允许你使用没有事先定义的参数名:

def table_things(**kwargs):

    for name, value in kwargs.items():

        print '{0} = {1}'.format(name, value)


table_things(apple = 'fruit', cabbage = 'vegetable')

cabbage = vegetable

apple = fruit

你也可以混着用.命名参数首先获得参数值然后所有的其他参数都传递给*args和**kwargs.命名参数在列表的最前端.例如:

def table_things(titlestring, **kwargs)

*args和**kwargs可以同时在函数的定义中,但是*args必须在**kwargs前面.

当调用函数时你也可以用*和**语法.例如:
 def print_three_things(a, b, c):

    print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)

...

mylist = ['aardvark', 'baboon', 'cat']

print_three_things(*mylist)

 

a = aardvark, b = baboon, c = cat

就像你看到的一样,它可以传递列表(或者元组)的每一项并把它们解包.注意必须与它们在函数里的参数相吻合.当然,你也可以在函数定义或者函数调用时用*.
'''