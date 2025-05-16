class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [0]*k 
        ans = [0]*k
        for a in nums:
            ndp = [0]*k 
            ndp[a%k] += 1
            for r in range(k):
                ndp[(r*a)%k] += dp[r]
            dp = ndp
            for r in range(k):
                ans[r] += dp[r]
        return ans 
