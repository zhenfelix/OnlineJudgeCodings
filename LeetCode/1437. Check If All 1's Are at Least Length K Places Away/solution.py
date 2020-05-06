# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         pre = -float('inf')
#         for i, num in enumerate(nums):
#             if num == 1:
#                 # print(pre)
#                 if i-pre <= k:
#                     return False
#                 pre = i
#         return True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ct = k+1
        for num in nums:
            if num == 1:
                if ct < k:
                    return False
                ct = 0
            else:
                ct += 1
        return True