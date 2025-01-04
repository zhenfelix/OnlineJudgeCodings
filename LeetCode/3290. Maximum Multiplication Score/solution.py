class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        @lru_cache(None)
        def dfs(i,j):
            if j == 0: return 0
            if i < 0: return -inf
            return max(dfs(i-1,j),dfs(i-1,j-1)+b[i]*a[j-1])
        ans = dfs(n-1,4)
        dfs.cache_clear()
        return ans