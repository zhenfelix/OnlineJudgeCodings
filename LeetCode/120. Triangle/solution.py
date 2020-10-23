class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf')]*n
        dp[0] = triangle[0][0]
        for i in range(1,n):
            j = i 
            while j >= 0:
                if j == 0:
                    dp[j] = dp[j]+triangle[i][j]
                elif j == i:
                    dp[j] = dp[j-1]+triangle[i][j]
                else:
                    dp[j] = min(dp[j]+triangle[i][j],dp[j-1]+triangle[i][j])
                j -= 1
        return min(dp)