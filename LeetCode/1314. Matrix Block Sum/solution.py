class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = mat[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]

        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                down, right = min(i+K+1,n), min(j+K+1,m)
                up, left = max(i-K,0), max(j-K,0)
                ans[i][j] = dp[down][right]+dp[up][left]-dp[up][right]-dp[down][left]
        return ans