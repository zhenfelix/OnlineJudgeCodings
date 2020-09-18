class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mp = {1: -1, -1: float('inf')}
        res, cur = 0, 1
        for i, x in enumerate(nums):
            if x > 0:
                cur *= 1
            elif x < 0:
                cur *= -1
            else:
                cur = 0
            if cur == 0:
                cur = 1
                mp = {1: i, -1: float('inf')}
            else:
                res = max(res, i-mp[cur])
                mp[cur] = min(mp[cur], i)
        return res
