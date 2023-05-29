class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        for s in range(1,1<<n):
            v = 1
            for i in range(n):
                if (s>>i)&1:
                    v *= nums[i]
            ans = max(ans,v)
        return ans 