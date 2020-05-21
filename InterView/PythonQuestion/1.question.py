'''
1 Python的函数参数传递

看两个例子:

a = 1

def fun(a):

    a = 2

fun(a)
print(a)


a = []

def fun(a):

    a.append(1)

fun(a)
print(a)

答： 第一个输出 a=1   第二个输出a=[1]
第一个在调用函数的时候只是在函数内部的内存地址发生改变，他和外面a=1没有任何关系 所以最后的输出并没有改变a=1的值，
第二个是对象发生改变 因为列表是可变对象，操作列表添加的方法将列表中的内存地址发生改变了

'''


'''

2 Python中的元类(metaclass)

这个非常的不常用,但是像ORM这种复杂的结构还是会需要的

答：
元类就是用来创建这些类（对象）的，元类就是类的类
类其实是能够创建出类实例的对象。事实上，类本身也是实例，当然，它们是元类的实例。
Python中的一切都是对象，它们要么是类的实例，要么是元类的实例，除了type。type实际上是它自己的元类，在纯Python环境中这可不是你能够做到的，这是通过在实现层面耍一些小手段做到的。其次，元类是很复杂的。对于非常简单的类，你可能不希望通过使用元类来对类做修改。
'''



'''
3 @staticmethod和@classmethod

Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:

def foo(x):

    print "executing foo(%s)"%(x)

 

class A(object):

    def foo(self,x):

        print "executing foo(%s,%s)"%(self,x)

 

    @classmethod

    def class_foo(cls,x):

        print "executing class_foo(%s,%s)"%(cls,x)

 

    @staticmethod

    def static_foo(x):

        print "executing static_foo(%s)"%x

 

a=A()

对于静态方法其实和普通的方法一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用a.static_foo(x)或者A.static_foo(x)来调用.

            实列方法        类方法           静态方法
a = A()     a.foo(x)      a.class_foo(x)    a.static_foo(x)

A           不可用         A.class_foo(x)    A.class_foo(x)
'''


'''
4 类变量和实例变量

类变量：

​ 是可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。例如下例中，num_of_instance 就是类变量，用于跟踪存在着多少个Test 的实例。

实例变量：

实例化之后，每个实例单独拥有的变量。

class Test(object): 

    num_of_instance = 0 

    def __init__(self, name): 

        self.name = name 

        Test.num_of_instance += 1 

 

if __name__ == '__main__': 

    print Test.num_of_instance   # 0

    t1 = Test('jack') 

    print Test.num_of_instance   # 1

    t2 = Test('lucy') 

    print t1.name , t1.num_of_instance  # jack 2

    print t2.name , t2.num_of_instance  # lucy 2

    

补充的例子

class Person:

    name="aaa"

 

p1=Person()

p2=Person()

p1.name="bbb"

print p1.name  # bbb

print p2.name  # aaa

print Person.name  # aaa

这里p1.name="bbb"是实例调用了类变量,因为实例化P1之后改变了name 的值  所以 P1.name就不会在调用类中的name 反而会输出修改后的值，而P2 并没有改变name的值  

可以看看下面的例子:

class Person:

    name=[]

 

p1=Person()

p2=Person()

p1.name.append(1)

print p1.name  # [1]

print p2.name  # [1]

print Person.name  # [1]

由于name中的是列表，当P1实例化之后添加了name 列表中的值，此时name列表的值已经发生改变，共享给了每一个单条实例。因此不管是哪个实例化调用name的值总是会输出 [1]
'''


'''
5 Python自省

这个也是python彪悍的特性.

自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型.简单一句就是运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().

a = [1,2,3]

b = {'a':1,'b':2,'c':3}

c = True

print type(a),type(b),type(c) # <type 'list'> <type 'dict'> <type 'bool'>

print isinstance(a,list)  # True
'''