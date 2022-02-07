class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot = sum(nums)
        res = []
        mx = 0
        left = 0
        for i in range(n+1):
            if i > 0:
                left += nums[i-1]
            cur = i-left+tot-left
            if cur > mx:
                mx = cur
                res = [i]
            elif cur == mx:
                res.append(i)
        return res