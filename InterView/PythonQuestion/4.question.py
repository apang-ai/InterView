'''
16 单例模式

​ 单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例

1 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):

        if not hasattr(cls, '_instance'):
            orig = super(Singlenton, cls)
            cls._instance = prig.__new__(cls, *args, **kw)
        
        return cls._instance

class Myclass(Singleton):
    a = 1


2、共享属性
创建实例时把所有实例的__dict__指向同一个字典，这样他们具有相同的属性和方法
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):

    a = 1


3 装饰器版本

def singleton(cls):

    instances = {}

    def getinstance(*args, **kw):

        if cls not in instances:

            instances[cls] = cls(*args, **kw)

        return instances[cls]

    return getinstance

 

@singleton

class MyClass:

  ...


4 import方法

作为python的模块是天然的单例模式

# mysingleton.py

class My_Singleton(object):

    def foo(self):

        pass

 

my_singleton = My_Singleton()

 

# to use

from mysingleton import my_singleton

 

my_singleton.foo()

 17 Python中的作用域

Python 中，一个变量的作用域总是由在代码中被赋值的地方所决定的。

当 Python 遇到一个变量的话他会按照这样的顺序进行搜索：

本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）

18 GIL线程全局锁

线程全局锁(Global Interpreter Lock),即Python为了保证线程安全而采取的独立线程运行的限制,说白了就是一个核只能在同一时间运行一个线程.对于io密集型任务，python的多线程起到作用，但对于cpu密集型任务，python的多线程几乎占不到任何优势，还有可能因为争夺资源而变慢。

见Python 最难的问题

解决办法就是多进程和下面的协程(协程也只是单CPU,但是能减小切换代价提升性能).

19 协程

知乎被问到了,呵呵哒,跪了

简单点说协程是进程和线程的升级版,进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间,而协程就是用户自己控制切换的时机,不再需要陷入系统的内核态.

Python里最常见的yield就是协程的思想!可以查看第九个问题.

20 闭包

闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

当一个内嵌函数引用其外部作作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:

必须有一个内嵌函数
内嵌函数必须引用外部函数中的变量
外部函数的返回值必须是内嵌函数
感觉闭包还是有难度的,几句话是说不明白的,还是查查相关资料.

重点是函数运行后并不会被撤销,就像16题的instance字典一样,当函数运行完后,instance并不被销毁,而是继续留在内存空间里.这个功能类似类里的类变量,只不过迁移到了函数上.

闭包就像个空心球一样,你知道外面和里面,但你不知道中间是什么样.


'''