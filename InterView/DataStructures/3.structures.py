'''
leetcode: 
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


class Solution:
    def climbStairs(self, n: int) -> int:
        # 由题意可知： 1  1种; 2：2种； 3: 3种； 4:5种；以此类推
        # 方法就可以表示  1 2 3 5 8   最后的方法数就是前两位数相加的和
        # 因此在列表中 不断的把最后两位数加起来 即： list_nums[-1] + lsit_nums[-2], 最后返回的结果是最后一个的值
        # 保持列表中有最开始的两位数
        list_num = [0, 1]

        for i in range(n):
            
            list_num.append(list_num[-1] + list_num[-2])
            print(list_num)

        return list_num[-1]

'''


'''
面试题64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000


'''

# 看题意得知  这是一个算数相加的题 
# n= 3  就是 3+(3-1)+((3-1)-1)
# 用递归的思想去解决问题， 判断 如果当 n = 1的时候结束递归
def intger_sum(n):

    if n == 1:

        return n
    
    return n + intger_sum(n-1)

print(intger_sum(9))
