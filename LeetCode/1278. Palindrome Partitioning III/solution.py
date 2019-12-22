from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        @lru_cache(None)
        def dfs(i,j,k):
            # print(i,j,k)
            if k > j-i+1 and i <= j:
                # print(i,j,k)
                return float('inf')
            if k == 1:
                if i >= j:
                    return 0
                return dfs(i+1,j-1,k) + (1 if s[i]!=s[j] else 0)
            # print(i,j,k,[(i,j,mid,dfs(i,mid,1),dfs(mid+1,j,k-1)) for mid in range(i,j)])
            res = min([dfs(i,mid,1)+dfs(mid+1,j,k-1) for mid in range(i,j)])
            # print(i,j,res)
            return res

        return dfs(0,len(s)-1,K)
