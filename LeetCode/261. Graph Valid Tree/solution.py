class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges)+1:
            return False
        def dfs(cur,visited):
            visited.add(cur)
            for nxt in g[cur]:
                if nxt not in visited:
                    dfs(nxt,visited)
            return 
        visited = set()
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        dfs(0, visited)
        return len(visited) == n