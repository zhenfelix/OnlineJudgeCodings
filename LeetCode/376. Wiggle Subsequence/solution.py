# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         up, down = [0]*n, [0]*n
#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     up[i] = max(up[i], down[j]+1)
#                 elif nums[i] < nums[j]:
#                     down[i] = max(down[i], up[j]+1)
#         return 1+max(up+down)
        
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         up, down = 0, 0
#         for i in range(1,n):
#             if nums[i] > nums[i-1]:
#                 up = down+1
#             elif nums[i] < nums[i-1]:
#                 down = up+1
#         return 1+max(up,down)

class Solution:
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0
        
        length = 1
        up = None # current is neither increasing nor decreasing
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length
    
# Greedy, the longest wiggle subsequence always ends with the last character
        