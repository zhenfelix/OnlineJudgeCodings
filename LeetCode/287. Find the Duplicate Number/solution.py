class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        lo, hi = 1, n 
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = sum(x <= mid for x in nums)
            if cnt <= mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo