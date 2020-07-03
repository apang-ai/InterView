'''
108. 将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
 '''


 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def treeRoot(startIndex, endIndex):
            # 判断开始的索引位置必须小于最后索引位置，否知不存在返回 None
            if startIndex > endIndex:

                return None

            # 求出初始的树的根即中间数
            midIndex = (startIndex + endIndex)//2
            # 做一个初始树
            thisTree = TreeNode(nums[midIndex])

            thisTree.left = treeRoot(startIndex, midIndex-1)
            thisTree.right = treeRoot(midIndex+1, endIndex)

            # 返回这个树
            return thisTree

        # 整个题解只和index有关，和数组里的具体数字无关，
        # 因为题目给出的“有序数列”帮助我们满足了“二叉搜索树”的条件。
        return treeRoot(0, len(nums)-1)


# 递给的思路解决

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums: 
            return None

        mid = (len(nums)-1)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# [-10,-3,0,5,9]