class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        edges = set()
        for a, b in connections:
            edges.add((a,b))
            g[a].append(b)
            g[b].append(a)
        res = 0

        def dfs(cur,parent):
            nonlocal res
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                if (cur,nxt) in edges:
                    res += 1
                dfs(nxt,cur)
            return

        dfs(0,-1)
        return res