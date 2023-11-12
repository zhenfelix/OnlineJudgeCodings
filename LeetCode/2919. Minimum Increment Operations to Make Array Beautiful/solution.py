class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        nums.append(inf)
        for i in range(n+1):
            dp[i] = min(dp[i-1-j] for j in range(3))+max(0,k-nums[i])

        return dp[-1]