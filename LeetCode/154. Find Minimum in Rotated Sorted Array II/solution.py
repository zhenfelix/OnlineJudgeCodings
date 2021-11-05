class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi and nums[lo] == nums[hi]:
            hi -= 1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
        # print(lo,hi)
        return nums[lo%n]

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         n = len(nums)
#         lo, hi = 0, n-1
#         while lo + 1 < hi:
#             mid = (lo+hi)//2
#             if nums[lo] < nums[hi]:
#                 break
#             elif nums[lo] < nums[mid]:
#                 lo = mid
#             else:
#                 hi  = mid
#         return min(nums[lo],nums[hi])

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo + 1 < hi:
            while lo + 1 < hi and nums[lo] == nums[lo+1]:
                lo += 1
            while lo + 1< hi and nums[hi-1] == nums[hi]:
                hi -= 1
            if lo +1 >= hi:
                break
            mid = (lo+hi)//2
            if nums[lo] < nums[hi]:
                break
            elif nums[lo] < nums[mid]:
                lo = mid
            else:
                hi  = mid
        return min(nums[lo],nums[hi])