class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))
        cnt = [0]*n
        res = 0
        def dfs(cur,sums,cost):
            nonlocal res
            if cost > maxTime:
                return
            if cnt[cur] == 0:
                sums += values[cur]
            cnt[cur] += 1
            if cur == 0:
                res = max(res, sums)
            for nxt, t in graph[cur]:
                dfs(nxt,sums,cost+t)
            cnt[cur] -= 1
            return
        dfs(0,0,0)
        return res
