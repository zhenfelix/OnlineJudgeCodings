class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
        arr = sorted(g, key=lambda x: -len(g[x]))
        n = len(arr)
        if len(g[arr[0]]) != n-1:
            return 0
        ans = 1
        for a, b in pairs:
            if len(g[a]) == len(g[b]):
                ans = 2
        parent = {x: arr[0] for x in arr}
        visited = set([arr[0]])
        for cur in arr[1:]:
            for nxt in g[cur]:
                if nxt not in visited:
                    if parent[cur] != parent[nxt]:
                        return 0
                    parent[nxt] = cur
            visited.add(cur)
        return ans

