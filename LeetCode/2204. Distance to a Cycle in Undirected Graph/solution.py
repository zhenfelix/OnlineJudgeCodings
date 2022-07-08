class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        color = [0]*n 
        cycle = set()
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(cur, parent, path):
            path.append(cur)
            color[cur] = 1
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                if color[nxt] == 1:
                    while path:
                        tmp = path.pop()
                        cycle.add(tmp)
                        if tmp == nxt:
                            return True
                if color[nxt] == 0:
                    if dfs(nxt,cur,path):
                        return True
            color[cur] = 2
            path.pop()
            return False

        dfs(0,-1,[])
        # print(cycle)
        q = [i for i in range(n) if i in cycle]
        visited = set(q)
        ans = [-1]*n 
        dist = 0
        while q:
            nq = []
            for cur in q:
                ans[cur] = dist
                for nxt in g[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        nq.append(nxt)
            q = nq 
            dist += 1
        return ans