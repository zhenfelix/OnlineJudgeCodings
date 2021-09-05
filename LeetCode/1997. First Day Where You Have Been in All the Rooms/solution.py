class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9+7
        n = len(nextVisit)
        dp = [0]*n 
        for i in range(1,n):
            dp[i] = dp[i-1]*2-dp[nextVisit[i-1]]+2
            dp[i] %= MOD
        return dp[-1]