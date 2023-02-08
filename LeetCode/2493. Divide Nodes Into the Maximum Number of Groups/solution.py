class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        parent = list(range(n))
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return  

        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
            connect(u,v)
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        def bfs(r):
            dist = [-1]*n 
            dist[r] = 0
            q = [r]
            while q:
                # print(r,dist)
                nq = []
                for x in q:
                    for y in g[x]:
                        if dist[y] == -1:
                            dist[y] = dist[x] + 1
                            nq.append(y)
                        elif abs(dist[y]-dist[x]) != 1:
                            return -1
                q = nq 

            return max(dist)+1

        ans = 0
        for k, v in groups.items():
            # print(v)
            tmp = max(bfs(i) for i in v)
            if tmp == -1:
                return -1
            ans += tmp 
        return ans 