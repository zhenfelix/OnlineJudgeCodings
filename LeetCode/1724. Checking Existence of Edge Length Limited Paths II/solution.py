inf = sys.maxsize
class DistanceLimitedPathsExist:
    def find(self, i, mt=inf):
        return i if i == self.f[i] or self.t[i] >= mt else self.find(self.f[i], mt)
    
    def union(self, i, j, t):
        fi, fj = self.find(i), self.find(j)
        if fi != fj:
            if self.m[fj] > self.m[fi]:
                self.t[fi] = t
                self.f[fi] = fj
            else:
                self.t[fj] = t
                self.f[fj] = fi
            if self.m[fi] == self.m[fj]:
                self.m[fi] += 1

    def __init__(self, n: int, edgeList: List[List[int]]):
        edgeList.sort(key=lambda it:it[2])
        f = list(range(n)) # 集合的根
        m = [0] * n # 树的深度
        t = [inf - 1] * n # 合并的时间戳
        self.f = f
        self.m = m
        self.t = t
        for u, v, t in edgeList:
            self.union(u, v, t)

    def query(self, p: int, q: int, limit: int) -> bool:
        return self.find(p, limit) == self.find(q, limit)


# 作者：megurine
# 链接：https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths-ii/solution/ke-chi-jiu-hua-bing-cha-ji-by-megurine-l1m6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        parent = [i for i in range(n)]
        g = defaultdict(list)
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        for a, b, dist in sorted(edgeList, key = lambda x: x[-1]):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                g[a].append((b,dist))
                g[b].append((a,dist))

        m = 0
        while 2**m+1 <= n:
            m += 1
        self.ancestors = [[-1]*m for _ in range(n)]
        self.weights = [[0]*m for _ in range(n)]
        self.tin = [-1]*n 
        self.tout = [-1]*n 
        clock = 0

        def dfs(cur, pre, dist):
            nonlocal clock
            clock += 1
            self.tin[cur] = clock
            u = cur
            self.ancestors[u][0] = pre
            self.weights[u][0] = dist
            for j in range(1,m):
                self.ancestors[u][j] = self.ancestors[self.ancestors[u][j-1]][j-1]
                self.weights[u][j] = max(self.weights[u][j-1], self.weights[self.ancestors[u][j-1]][j-1])
            for nxt, w in g[cur]:
                if nxt == pre:
                    continue
                dfs(nxt, cur, w)
            clock += 1
            self.tout[cur] = clock
            return

        for i in range(n):
            if parent[i] == i:
                for j in range(m):
                    self.ancestors[i][j] = i
                dfs(i,i,0)
        
        # print(parent)
        # print(self.ancestors)
        # print(self.weights)


    def query(self, p: int, q: int, limit: int) -> bool:
        if self.ancestors[p][-1] != self.ancestors[q][-1]:
            return False
        root = self.ancestors[p][-1]
        m = len(self.ancestors[0])

        def isAncestor(u,v):
            return self.tin[u] <= self.tout[v] and self.tout[u] >= self.tout[v]

        def lca(u,v):
            mx = 0
            for j in range(m)[::-1]:
                if not isAncestor(self.ancestors[u][j],v):
                    mx = max(mx, self.weights[u][j])
                    u = self.ancestors[u][j]
            mx = max(mx,self.weights[u][0])
            return mx 

        if isAncestor(p,q):
            return lca(q,p) < limit
        elif isAncestor(q,p):
            return lca(p,q) < limit
        else:
            return max(lca(q,p),lca(p,q)) < limit






# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)
