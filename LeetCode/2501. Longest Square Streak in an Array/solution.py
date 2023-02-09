class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        cc = dict()
        for v in nums:
            if v in cc:
                cc[v*v] = cc[v]+1
            else:
                cc[v*v] = 1
        ans = max(cc.values())
        return ans if ans >= 2 else -1