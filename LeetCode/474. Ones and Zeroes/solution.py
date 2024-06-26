# from collections import Counter
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         w = [(x['0'],x['1']) for x in map(Counter, strs)]
#         # print(w)
#         def dfs(idx, x, y):
#             if (idx,x,y) in memo:
#                 return memo[idx,x,y]
#             if idx == -1:
#                 memo[idx,x,y] = 0
#                 return 0
#             # if x <= 0 and y <= 0:
#             #     memo[idx,x,y] = 0
#             #     return 0
#             memo[idx,x,y] = dfs(idx-1,x,y)
#             if x-w[idx][0] >= 0 and y-w[idx][1] >= 0:
#                 memo[idx,x,y] = max(memo[idx,x,y],dfs(idx-1,x-w[idx][0],y-w[idx][1])+1)
#             return memo[idx,x,y]

#         memo = {}
#         dfs(len(w)-1,m,n)
#         # print(memo)
#         return memo[len(w)-1,m,n]

class Solution(object):
    def findMaxForm(self, strs, m, n):
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
        return dp[m][n]


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sz = len(strs)
        cnt = [[0]*2 for _ in range(sz)]
        for i, s in enumerate(strs):
            for ch in s:
                cnt[i][ord(ch)-ord('0')] += 1
        @lru_cache(None)
        def dfs(i, mm, nn):
            if mm < 0 or nn < 0:
                return -float('inf')
            if i == sz:
                return 0 if mm >= 0 and nn >= 0 else -float('inf')
            return max(dfs(i+1, mm-cnt[i][0], nn-cnt[i][1])+1, dfs(i+1, mm, nn))
        return dfs(0,m,n)