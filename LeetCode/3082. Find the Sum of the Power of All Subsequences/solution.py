class Solution:
    def sumOfPower(self, nums: List[int], K: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        @lru_cache(None)
        def dfs(i,k):
            if i < 0:
                return 1 if k == 0 else 0
            if k < 0:
                return 0

            return (dfs(i-1,k)*2+dfs(i-1,k-nums[i]))%MOD
        return dfs(n-1,K)
