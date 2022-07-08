class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        m = 0
        while (1<<m)+1 <= n:
            m += 1
        m += 1
        ancestor = [[0]*m for _ in range(n)]
        tin = [-1]*n 
        tout = [-1]*n 
        clock = 0
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(cur, parent):
            nonlocal clock
            clock += 1
            tin[cur] = clock
            ancestor[cur][0] = parent
            for i in range(1,m):
                ancestor[cur][i] = ancestor[ancestor[cur][i-1]][i-1]
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(nxt, cur)
            clock += 1
            tout[cur] = clock
            return  

        def isAncestor(x, y):
            return tin[x] <= tin[y] and tout[x] >= tout[y]

        def lca(x, y):
            for i in range(m)[::-1]:
                if not isAncestor(ancestor[x][i], y):
                    x = ancestor[x][i]
            x = ancestor[x][0]
            return x 

        ans = []
        dfs(0,0)
        for u, v, q in query:
            if isAncestor(v, u):
                u, v = v, u 
            if isAncestor(u, v):
                if isAncestor(u, q):
                    if isAncestor(v, q):
                        ans.append(v)
                    else:
                        ans.append(lca(v,q))
                else:
                    ans.append(u)
            else:
                if isAncestor(u,q):
                    ans.append(u)
                elif isAncestor(v,q):
                    ans.append(v)
                else:
                    p = lca(u,v)
                    if isAncestor(p,q):
                        tmp = lca(u,q)
                        if tmp == p:
                            ans.append(lca(v,q))
                        else:
                            ans.append(tmp)
                    else:
                        ans.append(p)
        return ans