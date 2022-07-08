class Solution:
    def countSubranges(self, a: List[int], b: List[int]) -> int:
        MOD = 10**9+7
        ans = 0 
        dp = defaultdict(int)
        for aa, bb in zip(a,b):
            ndp = defaultdict(int)
            dp[0] += 1
            for k, v in dp.items():
                ndp[k+aa] += v
                ndp[k-bb] += v 
            dp = ndp
            ans += dp[0]
            ans %= MOD
            # print(dp)
        return ans