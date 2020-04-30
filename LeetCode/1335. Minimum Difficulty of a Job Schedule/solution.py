from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], D: int) -> int:
        @lru_cache(None)
        def dfs(n,d):
            if d > n:
                return -1
            if n == 0:
                return 0
            if d == 0:
                return -1
            right, res = 0, float('inf')
            for i in range(n)[::-1]:
                right = max(right,jobDifficulty[i])
                if dfs(i,d-1) > -1:
                    res = min(res, dfs(i,d-1)+right)
            return res if res != float('inf') else -1
        return dfs(len(jobDifficulty), D)