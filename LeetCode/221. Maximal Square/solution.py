from __future__ import annotations
from pprint import pprint


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m==0:
            return 0
        n = len(matrix[0])
        dp = [[ 0 for j in range(0, n+1)] for i in range(0, m+1)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]=='1'):
                    dp[i][j]=min(min(dp[i-1][j-1],dp[i-1][j]),dp[i][j-1])+1
                    ans=max(ans,dp[i][j])
        return ans*ans


mat=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
s.maximalSquare(mat)