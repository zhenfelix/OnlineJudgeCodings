class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
        ans = -inf
        @lru_cache(None)
        def dfs(u,r,limit):
            if limit <= 0:
                return -inf
            if r == 0:
                return 0
            res = -inf
            for v,w in g[u]:
                res = max(res,dfs(v,r-1,limit-w)+w)
            return res 
        for i in range(n):
            ans = max(ans,dfs(i,k,t))
        return ans if ans > -inf else -1
