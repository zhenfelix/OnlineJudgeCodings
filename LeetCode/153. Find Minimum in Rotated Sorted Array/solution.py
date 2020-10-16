class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo + 1 < hi:
            mid = (lo+hi)//2
            if nums[lo] < nums[hi]:
                break
            elif nums[lo] < nums[mid]:
                lo = mid
            else:
                hi  = mid
        return min(nums[lo],nums[hi])