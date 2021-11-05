class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        mi = float('inf')
        for x in nums:
            mi = min(mi, x)
            if x > mi:
                res = max(res, x-mi)
        return res