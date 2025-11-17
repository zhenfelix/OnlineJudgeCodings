class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = defaultdict(list)
        parent = [0]*n  
        for u, v in hierarchy:
            u -= 1
            v -= 1
            g[u].append(v)
            parent[v] = u

        @lru_cache(None)
        def dfs1(cur,flag,b):
            cost = present[cur]//2 if flag else present[cur]
            ans = dfs2(cur,0,0,b)
            if cost <= b:
                ans = max(ans,dfs2(cur,0,1,b-cost)+future[cur]-cost)
            return ans 

        @lru_cache(None)
        def dfs2(cur,i,flag,b):
            m = len(g[cur])
            if i == m: return 0 
            nxt = g[cur][i]
            if nxt == parent[cur]: return dfs2(cur,i+1,flag,b)
            ans = 0
            for nb in range(b+1):
                ans = max(ans,dfs1(nxt,flag,nb)+dfs2(cur,i+1,flag,b-nb))
            return ans 

        res = dfs1(0,0,budget)
        dfs1.cache_clear()
        dfs2.cache_clear()
        return res 

