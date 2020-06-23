'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

'''

'''
解题思路： 将列表中的数转化成字符串，再转成整数 +1 之后再转成列表返回

'''

def plusOne(digits):

    numStr = ''
    for i in digits:
        numStr += str(i)

    newNumStr = int(numStr) + 1

    return [int(i) for i in str(newNumStr)]

digits = [1, 2, 9]

plusOne(digits)