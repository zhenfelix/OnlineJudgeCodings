class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dp = defaultdict(int)
        ans = 0
        for i in range(n)[::-1]:
            v = nums[i]
            dp[v] = max(dp[v],1+dp[v+1])
            ans = max(ans,dp[v])
            v += 1
            dp[v] = max(dp[v],1+dp[v+1])
            ans = max(ans,dp[v])
        return ans 