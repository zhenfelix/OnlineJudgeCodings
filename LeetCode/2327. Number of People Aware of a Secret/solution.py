class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9+7
        f = [0]*n 
        f[0] = 1
        for i in range(n):
            for j in range(i+delay,min(i+forget,n)):
                f[j] = (f[j]+f[i])%MOD
        return sum(f[-forget:])%MOD 


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9+7
        f = [0]*(n+1) 
        f[1] = 1
        for i in range(2,n+1):
            f[i] = (f[max(i-delay,0)]-f[max(i-forget,0)]+f[i-1])%MOD
        return (f[n]-f[max(n-forget,0)])%MOD


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0]*n 
        dp[0] = 1
        for i in range(1,n):
            if i-delay >= 0:
                dp[i] = dp[i-delay]-(dp[i-forget] if i-forget >= 0 else 0)+MOD
            dp[i] += dp[i-1]
            dp[i] %= MOD
        # print(dp)
        return (dp[-1]-(dp[-forget-1] if forget < n else 0)+MOD)%MOD




class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0]*n 
        dp[0] = 1
        for i in range(1,n):
            for j in range(i):
                if i-j >= delay and i-j < forget:
                    dp[i] += dp[j]
            dp[i] %= MOD
        # print(dp)
        return sum(dp[-forget:])%MOD

