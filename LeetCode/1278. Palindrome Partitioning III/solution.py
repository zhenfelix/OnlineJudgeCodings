# from functools import lru_cache
# class Solution:
#     def palindromePartition(self, s: str, K: int) -> int:
#         @lru_cache(None)
#         def dfs(i,j,k):
#             # print(i,j,k)
#             if k > j-i+1 and i <= j:
#                 # print(i,j,k)
#                 return float('inf')
#             if k == 1:
#                 if i >= j:
#                     return 0
#                 return dfs(i+1,j-1,k) + (1 if s[i]!=s[j] else 0)
#             # print(i,j,k,[(i,j,mid,dfs(i,mid,1),dfs(mid+1,j,k-1)) for mid in range(i,j)])
#             res = min([dfs(i,mid,1)+dfs(mid+1,j,k-1) for mid in range(i,j)])
#             # print(i,j,res)
#             return res

#         return dfs(0,len(s)-1,K)


from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        
        def cost(i,j): #calculate the cost of transferring one substring into palindrome string
            if (i,j) in memo:
                return memo[i,j]
            r = 0
            if i >= j:
                return 0
            memo[i,j] = cost(i+1,j-1) + (s[i]!=s[j])
            return memo[i,j]
        
        @lru_cache(None)
        def dfs(i, k):
            if n - i == k: #base case that each substring just have one character
                return 0
            if k == 1:    #base case that need to transfer whole substring into palidrome
                return cost(i, n - 1)
            res = float('inf')
            for j in range(i + 1, n - k + 2): # keep making next part of substring into palidrome
                res = min(res, dfs(j, k - 1) + cost(i, j - 1)) #compare different divisions to get the minimum cost
            return res
        return dfs(0 , k)
# I really appreciate it if u vote up! （￣︶￣）↗