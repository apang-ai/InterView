'''
两个数组的交集 II

给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

'''

'''
解题思路：
先排序两个列表

设置公共列表 comment

定义两个指针初始值为0

循环 小于列表的长度
判断如果列表1的值小于列表2的值，则增加列表1的指针

如果两数相同，将它的值放入公共列表中

如果列表1的值大于列表2的值，则增加列表2的指针

最后返回列表

'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):

        nums1.sort()
        nums2.sort()

        comment = []

        right = 0
        left = 0

        while right < len(nums1) and left < len(nums2):

            if nums1[right] < nums2[left]:

                right += 1

            elif nums1[right] == nums2[left]:

                comment.append(nums1[right])

                right += 1
                left += 1

            else:
                left += 1

        return comment