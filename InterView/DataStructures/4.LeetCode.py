'''
13. 罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3

题解：

def romanToInt(self, s: str):

    # 定义一个字典，将每个罗马字符代表的值代表出来
    dic = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    # 定义最初使值为0
    value = 0
    # 遍历字符串的长度，排除掉最后一个，
    # 因为之后要用 s[i+1]来表示最后一位，
    # 如果这里没有 -1 那没字符长度运行到最后一位的时候会超出索引范围报错
    for i in range(len(s)-1):
        # 比较第一位的值如果大于等于第二位置，就把值相加
        if dic[s[i]] >= dic[s[i+1]]:
            value += dic[s[i]]

        # 否则值相减
        else:
            value -= dic[s[i]]
    
    # 因为之前把最后一位的值算进去，所以最后将最后一位加入值中
    value += dic[s[-1]]

    return value
'''


'''
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

题解：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)

            return l1

        else:

            l2.next = self.mergeTwoLists(l1, l2.next)

            return l2
'''


'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。


题解：

'''
def pop_nums(nums):

    if not nums: return []

    for index in range(len(nums)-1, 0, -1):

        if nums[index] == nums[index-1]:

            nums.pop(nums[index])

    return nums

nums = [1,1,2,3,3,4]

print(pop_nums(nums))

