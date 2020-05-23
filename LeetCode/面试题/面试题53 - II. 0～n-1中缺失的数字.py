class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo