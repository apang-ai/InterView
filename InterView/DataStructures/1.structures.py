
# def bubble_sort(nums):
#     for i in range(len(nums) - 1):
#         print('i:',i)
#         print(nums)
#         for j in range(len(nums) - i - 1):
#             print('j:',j)
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums

# print(bubble_sort(nums))
# def quick_sort(data):    
#     """快速排序"""    
#     if len(data) >= 2:
#         mid = data[0]
#         left, right = [], []
#         data.remove(mid)
#         for num in data:

#             if num >= mid:

#                 right.append(num)
#             else:
#                 left.append(num)
        
#         return quick_sort(left) + [mid] + quick_sort(right)
#     else:

#         return data
# nums = [3,6,4,2,11,5,10]
# print(quick_sort(nums))

