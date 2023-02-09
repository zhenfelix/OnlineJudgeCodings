class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x - 1].append((y - 1, d))
            g[y - 1].append((x - 1, d))
        ans = inf
        vis = [False] * n
        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)
        dfs(0)
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/T0eOvC/view/WCSm5y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union = UnionFind(n+1)
        for x, y, v in roads: union.merge(x, y)
        return min(v for x, y, v in roads if union.find(x) == union.find(1))


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/T0eOvC/view/CXzRey/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads = [(c,u-1,v-1) for u, v, c in roads]
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
        roads.sort()
        for c, u, v in roads:
            connect(u,v)
        
        for c2, u2, v2 in roads:
            if find(0) == find(u2):
                return c2

        return -1