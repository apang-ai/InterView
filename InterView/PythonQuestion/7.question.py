'''
Python是如何实现内存管理的？

> **点评**：当面试官问到这个问题的时候，一个展示自己的机会就摆在面前了。你要先反问面试官：“你说的是官方的CPython解释器吗？”。这个反问可以展示出你了解过Python解释器的不同的实现版本，而且你也知道面试官想问的是CPython。当然，很多面试官对不同的Python解释器底层实现到底有什么差别也没有概念。所以，**千万不要觉得面试官一定比你强**，怀揣着这份自信可以让你更好的完成面试。

Python提供了自动化的内存管理，也就是说内存空间的分配与释放都是由Python解释器在运行时自动进行的，自动管理内存功能极大的减轻程序员的工作负担，也能够帮助程序员在一定程度上解决内存泄露的问题。以CPython解释器为例，它的内存管理有三个关键点：引用计数、标记清理、分代收集。
'''

'''
#### 说一下你对Python中迭代器和生成器的理解。

> **点评**：很多人面试者都会写迭代器和生成器，但是却无法准确的解释什么是迭代器和生成器。如果你也有同样的困惑，可以参考下面的回答。

迭代器是实现了迭代器协议的对象。跟其他编程语言不通，Python中没有用于定义协议或表示约定的关键字，像`interface`、`protocol`这些单词并不在Python语言的关键字列表中。Python语言通过魔法方法来表示约定，也就是我们所说的协议，而`__next__`和`__iter__`这两个魔法方法就代表了迭代器协议。可以通过`for-in`循环从迭代器对象中取出值，也可以使用`next`函数取出迭代器对象中的下一个值。生成器是迭代器的语法升级版本，可以用更为简单的代码来实现一个迭代器。

> **扩展**：面试中经常让写生成斐波那契数列的迭代器，大家可以参考下面的代码。
>
> ```Python
> class Fib(object):
>  
>  def __init__(self, num):
>      self.num = num
>      self.a, self.b = 0, 1
>      self.idx = 0
> 
>  def __iter__(self):
>      return self
> 
>  def __next__(self):
>      if self.idx < self.num:
>          self.a, self.b = self.b, self.a + self.b
>          self.idx += 1
>          return self.a
>      raise StopIteration()
> ```
>
> 如果用生成器的语法来改写上面的代码，代码会简单优雅很多。
>
> ```Python
> def fib(num):
>  a, b = 0, 1
>  for _ in range(num):
>      a, b = b, a + b
>      yield a
> ```
'''


'''
正则表达式的match方法和search方法有什么区别？

> 正则表达式是字符串处理的重要工具，所以也是面试中经常考察的知识点。在Python中，使用正则表达式有两种方式，一种是直接调用`re`模块中的函数，传入正则表达式和需要处理的字符串；一种是先通过`re`模块的`compile`函数创建正则表达式对象，然后再通过对象调用方法并传入需要处理的字符串。**如果一个正则表达式被频繁的使用，我们推荐用`re.compile`函数创建正则表达式对象，这样会减少频繁编译同一个正则表达式所造成的开销**。

 `match`方法是从字符串的起始位置进行正则表达式匹配，返回`Match`对象或None。`search`方法会扫描整个字符串来找寻匹配的模式，同样也是返回Match对象或None。
'''