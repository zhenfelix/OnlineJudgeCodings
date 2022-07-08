class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        g = defaultdict(list)
        for a, b, w in highways:
            g[a].append((b,w))
            g[b].append((a,w))
        @cache
        def dfs(state, cur, r):
            if r == 0:
                return 0
            ans = -float('inf')
            for nxt, w in g[cur]:
                if (state>>nxt)&1:
                    continue
                ans = max(ans, w+dfs(state|(1<<nxt), nxt, r-1))
            return ans

        res = -float('inf')
        for i in range(n):
            res = max(res, dfs(1<<i, i, k))
        return res if res > -float('inf') else -1