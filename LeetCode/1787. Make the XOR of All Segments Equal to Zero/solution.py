class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        cnt, bucket, n = [Counter() for _ in range(k)], Counter(), len(nums)
        for i in range(n):
            bucket[i%k] += 1
            cnt[i%k][nums[i]] += 1
        dp = [float('inf')]*(1<<10)
        dp[0] = 0
        for i in range(k):
            lo = min(dp)
            ndp = [lo+bucket[i]]*(1<<10)
            for cur in range(1<<10):
                for val, freq in cnt[i].items():
                    pre = cur^val
                    ndp[cur] = min(ndp[cur], dp[pre]+bucket[i]-freq)
            dp = ndp
        return dp[0]