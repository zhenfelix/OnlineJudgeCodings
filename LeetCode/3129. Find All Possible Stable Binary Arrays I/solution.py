class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7


        @lru_cache(None)
        def dfs(i,j,ch):
            if i == 0:
                return ch == 1 and j <= limit
            if j == 0:
                return ch == 0 and i <= limit
            res = 0  
            if i > 0 and ch == 0:
                res += sum(dfs(k,j,1) for k in range(max(0,i-limit),i))
                res %= MOD
            if j > 0 and ch == 1:
                res += sum(dfs(i,k,0) for k in range(max(0,j-limit),j))
                res %= MOD
            return res  
        return (dfs(zero,one,0)+dfs(zero,one,1))%MOD


# class Solution:
#     def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
#         MOD = 10**9+7


#         @lru_cache(None)
#         def dfs(i,j,ii,jj):
#             if ii > limit or jj > limit: return 0
#             if i == 0:
#                 if j+jj > limit: return 0  
#                 return 1
#             if j == 0:
#                 if i+ii > limit: return 0
#                 return 1

#             ans = 0
#             if i > 0:
#                 ans += dfs(i-1,j,ii+1,0)
#             if j > 0:
#                 ans += dfs(i,j-1,0,jj+1)
#             return ans%MOD 
#         res = dfs(zero,one,0,0)
#         dfs.cache_clear()
#         return res