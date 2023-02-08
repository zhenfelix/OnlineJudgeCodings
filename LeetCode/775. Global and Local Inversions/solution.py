# class Solution:
#     def isIdealPermutation(self, nums: List[int]) -> bool:
#         mx = [nums[0], -1]
#         n = len(nums)
#         for i in range(1,n):
#             if mx[0] > nums[i]:
#                 if mx[0] != nums[i-1] or mx[-1] > nums[i]:
#                     return False
#                 mx[-1] = nums[i]
#             else:
#                 mx[-1] = mx[0]
#                 mx[0] = nums[i]
#         return True 

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        mx = -1
        n = len(nums)
        for i in range(1,n):
            if mx > nums[i]:
                return False
            mx = max(mx,nums[i-1])
        return True 

