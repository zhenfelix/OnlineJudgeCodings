class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, n//2
        while lo <= hi:
            m = (lo+hi)//2
            if all(a*2 <= b for a, b in zip(nums[:m],nums[-m:])):
                lo = m + 1
            else:
                hi = m - 1
        return hi*2 
