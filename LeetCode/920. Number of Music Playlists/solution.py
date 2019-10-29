from functools import reduce
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = collections.defaultdict(int)
        for n in range(1,N+1):
            # dp[n,n] = reduce(lambda a,b: a*b, [i for i in range(1,n+1)])
            dp[n,n] = reduce(lambda a,b: a*b, range(1,n+1))
            for l in range(n+1,L+1):
                # dp[n,l] = dp[n,l-1]*(n-K if n-K > 0 else 0) + dp[n-1,l-1]*n 
                dp[n,l] = dp[n,l-1]*max(n-K,0) + dp[n-1,l-1]*n 
        return dp[N,L]%(10**9+7)

