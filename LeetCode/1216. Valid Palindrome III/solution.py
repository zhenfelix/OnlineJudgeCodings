class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n and s[i] == s[i+1]:
                dp[i][i+1] = 2
        for t in range(n):
            for i in range(n-t):
                j = i + t
                if i > 0:
                    dp[i-1][j] = max(dp[i-1][j], dp[i][j])
                if j < n-1:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j])
                if i > 0 and j < n-1 and s[i-1] == s[j+1]:
                    dp[i-1][j+1] = max(dp[i-1][j+1], dp[i][j]+2)
        return n - dp[0][n-1] <= k


# class Solution:
#     def isValidPalindrome(self, s: str, k: int) -> bool:
#         def dfs(left, right, k):
#             if (left,right,k) in memo:
#                 return memo[left,right,k]
#             flag = False
#             if k < 0:
#                 flag = False
#             elif left >= right:
#                 flag = True
#             elif s[left] == s[right] and dfs(left+1, right-1, k):
#                 flag = True
#             elif dfs(left+1,right,k-1) or dfs(left,right-1,k-1):
#                 flag = True
                
#             memo[left,right,k] = flag
#             return flag
#         memo = {}
#         return dfs(0,len(s)-1,k)