class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        MOD = 10**9+7  
        for cnt, mark in types:
            ndp = [0]*(target+1)
            sums = [0]*mark
            for s in range(target+1):
                ss = s%mark
                sums[ss] = (sums[ss]+dp[s])%MOD
                if s-(cnt+1)*mark >= 0:
                    sums[ss] = (sums[ss]-dp[s-(cnt+1)*mark])%MOD
                ndp[s] = sums[ss]
            dp = ndp 
        return dp[-1]


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        MOD = 10**9+7  
        for cnt, mark in types:
            ndp = [0]*(target+1)
            for s in range(target+1)[::-1]:
                for i in range(cnt+1):
                    if s-i*mark < 0: break
                    ndp[s] = (ndp[s]+dp[s-i*mark])%MOD
            dp = ndp 
        return dp[-1]
