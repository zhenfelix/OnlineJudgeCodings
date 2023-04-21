class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        cnt = [0]*n 
        for start, end in trips:
            parent = [-1]*n 
            def dfs(cur,pre):
                parent[cur] = pre 
                for nxt in g[cur]:
                    if nxt == pre: continue
                    dfs(nxt,cur)
                return 
            dfs(start,start)
            cur = end 
            while parent[cur] != cur:
                cnt[cur] += 1
                cur = parent[cur]
            cnt[cur] += 1 
        
        # print(cnt)

        @lru_cache(None)
        def dp(cur,pre,s):
            res = 0
            for nxt in g[cur]:
                if nxt == pre: continue
                if s == 1:
                    res += dp(nxt,cur,0)
                else:
                    res += min(dp(nxt,cur,0),dp(nxt,cur,1))
            res += cnt[cur]*(price[cur]//2 if s else price[cur])
            # print(cur,pre,s,res)
            return res 
        return min(dp(0,0,1),dp(0,0,0))