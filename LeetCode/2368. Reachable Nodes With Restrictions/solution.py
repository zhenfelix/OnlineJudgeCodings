class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        restricted = set(restricted)
        def dfs(cur, parent):
            if cur in restricted:
                return 0
            ans = 1
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                ans += dfs(nxt, cur)
            return ans
        return dfs(0, 0)