import time
def timetest(fun):

    def warp(*args, **kwargs):

        time1 = time.time()
        fun(*args, **kwargs)
        time2 = time.time()

        time3 = time2 - time1
        print('函数运行时间为：%s'%time3)
    
    return warp



@timetest
def sum(li):
    su = 0
    for i in li:

        su += i
    print(su)
    # return su

sum([1,23,4,56,7,8,9,4,5,6,7,1,4])