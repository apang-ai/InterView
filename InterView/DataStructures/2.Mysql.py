# 在数据库中有⼀张叫做index_basic的表，它记录了各个指数数据的更新情况，⼜字段 updateTime表⽰最近更新⽇期。⼩明想要知道该表中那些指数没有被正确更新。他的想法是找出所有 updateTime在5⽇之前的记录，请问⽤SQL，他该如何实现？ 


# SELECT * FROM index_basic WHERE DETA(updateTime) =DATE_SUB(CURDATE(), INTERVAL 5 DAY)

# SELECT * FROM index_basic WHERE DATE(updateTime) =DATE_SUB(CURDATE(), INTERVAL 5 DAY)

# SELECT * FROM index_basic WHERE DATE(updateTime) = DATE_SUB(CURDATE(), INTERVAL 5 DAY)

# //获取前两天、、、、依次类推
# SELECT * FROM 表名 WHERE DATE(时间字段) =DATE_SUB(CURDATE(),INTERVAL 2 DAY) 


'''
写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变。

# def dedup(items):
#     no_dup_items = []
#     seen = set()
#     for item in items:
#         if item not in seen:
#             no_dup_items.append(item)
#             seen.add(item)
#     return no_dup_items


# items = [1,1,2,3,4,5,5,7,6,8,6]
# print(dedup(items))

'''


'''
假设你使用的是官方的CPython，说出下面代码的运行结果。

a, b, c, d =1, 1, 257, 257
print(a,b,c,d)
print(a is b, c is d)


def foo():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

foo()

上面代码中`a is b`的结果是`True`但`c is d`的结果是`False`，这一点的确让人费解。CPython解释器出于性能优化的考虑，把频繁使用的整数对象用一个叫`small_ints`的对象池缓存起来造成的。`small_ints`缓存的整数值被设定为`[-5, 256]`这个区间，也就是说，在任何引用这些整数的地方，都不需要重新创建`int`对象，而是直接引用缓存池中的对象。如果整数不在该范围内，那么即便两个整数的值相同，它们也是不同的对象。

'''