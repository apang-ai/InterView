'''
26 Python的is

is是对比地址,==是对比值

'''

'''
27 read,readline和readlines

read 读取整个文件
readline 读取下一行,使用生成器方法
readlines 读取整个文件到一个迭代器以供我们遍历

'''


'''
28 Python2和3的区别

Python 2.7.x 与 Python 3.x 的主要差异
1. Python 2中的print语句被Python 3中的print()函数取代，这意味着在Python 3中必须用括号将需要输出的对象括起来；

2. Python 2有基于ASCII的str()类型，其可通过单独的unicode()函数转成unicode类型，但没有byte类型。在Python 3中，终于有了Unicode（utf-8）字符串，以及两个字节类：bytes和bytearrays。

3. Python2.x中有xrange()和range(),xrange()是惰性机制的，如果只循环一次建议使用range(),对此的话range()会在内存中创建多尔列表，内存开销较大。python3中只有range()，range有了一个新的__contains__方法。__contains__方法可以有效的加快Python 3.x中整数和布尔型的“查找”速度。

4. 异常处理，在python3.x中必须使用‘as‘来处理， python2.x中可以不必使用

5. 在python2.x 中.Next()函数可以作为函数的属性使用，也可以单独作为函数使用；在python3.x 中只能使用函数，使用。Next()会触发attributeError.

6. python2.x中使用raw_input()解析用户输入，在python3.x 中使用input()解析

'''

'''
29 super init

1、如果子类(Puple)继承父类(Person)不做初始化(这里指的是子类中没有__init__初始化函数)，那么这时子类会自动继承父类(Person)属性name。 2、如果子类(Puple_Init)继承父类(Person)做了初始化(这里指的是子类中有__init__函数，对子类特有的属性进行了初始化)，且不调用super初始化父类构造函数，那么子类(Puple_Init)不会自动继承父类的属性(name)。 3、如果子类(Puple_super)继承父类(Person)做了初始化，且调用了super初始化了父类的构造函数，那么子类(Puple_Super)也会继承父类的(name)属性。注意：python3，super(子类名，self).__init__(父类属性)， 其中在子类初始化函数中要将父类的__init__函数中的父类属性全部包含进来；


Python2.7中的super方法浅见
'''

'''
30 range and xrange

都在循环时使用，xrange内存性能更好。
1.range([start], stop[, step])
返回等差数列。构建等差数列，起点是start，终点是stop，但不包含stop，公差是step。
start和step是可选项，没给出start时，从0开始；没给出step时，默认公差为1。


2.xrange([start], stop[, step])
xrange与range类似，只是返回的是一个"xrange object"对象，而非数组list。
要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。

区别：
1.range和xrange都是在循环中使用，输出结果一样。
2.range返回的是一个list对象，而xrange返回的是一个生成器对象(xrange object)。
3.xrange则不会直接生成一个list，而是每次调用返回其中的一个值，内存空间使用极少，因而性能非常好。

Python 3.x已经去掉xrange，全部用range代替。
'''