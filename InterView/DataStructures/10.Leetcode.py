'''
378. 有序矩阵中第K小的元素

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

'''


'''
left = matrix[0][0]
right = matrix[row-1][col-1]
mid = left + (right-left)//2
看了题解，自己尝试写，遇到两个问题：

1、如何确定matrix中有几个数比mid小？这个解决了。即为check函数。

2、如何避免找到的mid 不在矩阵中？这个问题是看了力扣官方题解的。
矩阵中的数和不在矩阵中的数的本质区别：
假设找到一个数mid，小于等于mid的数恰好是k,
-
- a)如果mid 不是矩阵中的值。那么必然有矩阵中小于等于mid +-epsilon范围内的值等于k
让mid 增大，大到mid就在矩阵中，此时矩阵中小于等于mid的数的个数会加1.
让mid 减小，小到mid就在矩阵中，此时mid就是我们需要求的值。
-
- b)如果mid是矩阵中的值，那么矩阵中小于等于mid-1的数的个数一定是k-1。
-
- 针对a),b)，我知道，拿到一个数mid，小于等于mid的值是k个。我只要再进一步缩小mid，使得小于等于mid的数恰好为k-1。那么mid+1一定是我要找的矩阵中的值。 转换成代码：


if check(mid,matrix)>=k:
    right=mid 缩小mid
else:
    left = mid+1 最终return的就是left值，也是当find结果<k后的mid+1的值

'''

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def check(mid):
            i, j = n - 1, 0
            res = 0
            while i >= 0 and j < n:
                if mid >= matrix[i][j]:
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            print(res, k)
            return res >= k
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            print(mid)
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left