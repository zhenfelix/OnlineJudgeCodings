# class Solution:
#     def longestPalindrome(self, word1: str, word2: str) -> int:
#         n, m = len(word1), len(word2)
#         s = word1 + word2
#         dp = [[0]*(n+m+1) for _ in range(n+m+1)]
#         for i in range(n+m)[::-1]:
#             pos = {}
#             end = n+m if i >= n else n 
#             for j in range(i,end):
#                 if s[j] not in pos:
#                     pos[s[j]] = j 
#                 left, right = pos[s[j]]+1, j-1
#                 dp[i][j] = max(dp[i][j-1],dp[left][right]+2+min(right-left+1,0))
#         pos = {}
#         for i in range(n)[::-1]:
#             pos[s[i]] = i 
#             for j in range(n,n+m):
#                 left, right = pos[s[j]]+1 if s[j] in pos else -1, j-1
#                 if left == -1:
#                     if j > n:
#                         dp[i][j] = dp[i][j-1]
#                 else:
#                     dp[i][j] = max(dp[i][j-1],dp[left][right]+2) if j > n else 2
#                     if left < n:
#                         dp[i][j] = max(dp[i][j],dp[left][n-1]+2)
#                     if right >= n:
#                         dp[i][j] = max(dp[i][j],dp[n][right]+2)


#         # print(n,m,dp)
#         return dp[0][n+m-1]

# class Solution:
#     def longestPalindrome(self, word1: str, word2: str) -> int:
#         n, m = len(word1), len(word2)
#         s = word1 + word2
#         dp = [[0]*(n+m+1) for _ in range(n+m+1)]
#         for i in range(n+m)[::-1]:
#             pos = {}
#             for j in range(i,n+m):
#                 if s[j] not in pos:
#                     pos[s[j]] = j 
#                 left, right = pos[s[j]]+1, j-1
#                 if i < n and j >= n:
#                     dp[i][j] = dp[i][j-1] if j > n else 0
#                     if left <= n:
#                         dp[i][j] = max(dp[i][j],dp[left][right]+2)
#                         if left < n:
#                             dp[i][j] = max(dp[i][j],dp[left][n-1]+2)
#                         if right >= n:
#                             dp[i][j] = max(dp[i][j],dp[n][right]+2)
#                 else:
#                     dp[i][j] = max(dp[i][j-1],dp[left][right]+2+min(right-left+1,0))
       
#         # print(n,m,dp)
#         return dp[0][n+m-1]


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        s = word1 + word2
        dp = [0 for j in range(n+m)]
        dp[-1] = 1
        res = 0
        for i in range(n+m)[::-1]:   
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i+1, n+m):

                if s[i] == s[j]:
                    newdp[j] = max(newdp[j], 2 + dp[j-1])
                    if i < n and j >= n:
                    #唯一的区别就在于当两端字符相等更新最长回文子串时
                    #若 i j 分别属于两个字符串，才更新最终结果值
                        res = max(res,newdp[j])
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
        # print(dp)
        return res