class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        res = 0
        for i in range(n):
            for j in range(m):
                cnt, k = 0, 0
                while i+k < n and j+k < m:
                    if s[i+k] != t[j+k]:
                        cnt += 1
                    if cnt > 1:
                        break
                    if cnt == 1:
                        res += 1
                    k += 1
        return res



from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @lru_cache(None)
        def dfs(i,j,diff):
            if i >= n or j >= m or diff < 0:
                return 0
            nxt = dfs(i+1,j,diff) + dfs(i,j+1,diff) - dfs(i+1,j+1,diff)
            contact = dfs(i+1,j+1,diff) - (dfs(i+2,j+1,diff)+dfs(i+1,j+2,diff)-dfs(i+2,j+2,diff))
            contact_ = dfs(i+1,j+1,diff-1) - (dfs(i+2,j+1,diff-1)+dfs(i+1,j+2,diff-1)-dfs(i+2,j+2,diff-1))
            if s[i] == t[j]:
                return nxt + contact + (diff == 0)
            else:
                return nxt + contact_ + (diff-1 == 0)
        return dfs(0,0,1)
