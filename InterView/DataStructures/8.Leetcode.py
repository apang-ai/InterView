'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

'''

'''
解题思路： 先求出给定的两个二进制的整数和，再转二进制

'''

def addBinary(a, b):
    if a == '0' and b == '0':
        return '0'
    else:
        # 给定的两个二进制和 设置初始值
        integer = 0
        # 遍历，二进制转整数 假如二进制 1 0   整数就为 0*2^0 + 1*2^1  和为 2  根据这样的求值方式 求出给定的两个二进制和
        for i in range(1, len(a)+1):
            integer += int(a[-i]) * pow(2, i-1)
        for i in range(1, len(b)+1):
            integer += int(b[-i]) * pow(2, i-1)
        # 给点两个二进制和 的二进制初始字符串空
        newInteger = ''
        # 判断当和一直大于0， 一直执行  
        # python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        # integer 就是一直要除以2的整数， z就代表余数，余数相加就是最后要表达的二进制数。
        while integer > 0:
            integer, z = divmod(integer, 2)
            newInteger = str(z) + newInteger
        return newInteger