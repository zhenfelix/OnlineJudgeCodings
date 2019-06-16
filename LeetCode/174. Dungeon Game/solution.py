class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        if n==0:
            return 0
        m = len(dungeon[0])
        NMAX=100000
        dp = [NMAX]*m
        dp[-1] = 1
        for r in range(n-1,-1,-1):
            dp[-1] = max(1,dp[-1]-dungeon[r][-1])
            for c in range(m-2,-1,-1):
                right=max(1,dp[c+1]-dungeon[r][c])
                down=max(1,dp[c]-dungeon[r][c])
                dp[c]=min(right,down)
            # print(dp)
        return dp[0]
                    
        