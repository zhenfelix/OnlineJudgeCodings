class DisjointSet:
    # 只用路径压缩的并查集
    def __init__(self, n):
        self.fa = [i for i in range(n + 1)]
    def add(self, u, v):
        u = self.father(u)
        v = self.father(v)
        if u == v:
            return False
        self.fa[u] = v
        return True
    def query(self, u, v):
        return self.father(u) == self.father(v)
    def father(self, u):
        if self.fa[u] == u:
            return u
        self.fa[u] = self.father(self.fa[u])
        return self.fa[u]
class Solution:
    def reservoir(self, shape: List[str]) -> int:
        def g(i, j, d):
            # 从二维坐标（以及分割的四个等腰直角三角形）对应到建的无向图编号
            return i * n * 4 + j * 4 + d
        m = len(shape)
        n = len(shape[0])
        total = m * n * 4 # 总结点数
        left = set() # 与左边界相邻的结点
        right = set() # 与右边界相邻的结点
        down = set() # 与下边界相邻的结点
        up = set() # 与上边界相邻的结点
        graph = [[] for i in range(total)] # 无向图，邻接表表示
        # 步骤I：构建无向图
        for i in range(m):
            for j in range(n):
                # 0, 1, 2, 3 直角三角形划分为逆时针方向，逐次与方格的左、下、右、上相邻
                if j > 0:
                    graph[g(i, j, 0)].append(g(i, j - 1, 2))
                else:
                    left.add(g(i, j, 0))
                if j < n - 1:
                    graph[g(i, j, 2)].append(g(i, j + 1, 0))
                else:
                    right.add(g(i, j, 2))
                if i > 0:
                    graph[g(i, j, 3)].append(g(i - 1, j, 1))
                else:
                    up.add(g(i, j, 3))
                if i < m - 1:
                    graph[g(i, j, 1)].append(g(i + 1, j, 3))
                else:
                    down.add(g(i, j, 1))
                if shape[i][j] != 'r':
                    graph[g(i, j, 0)].append(g(i, j, 1))
                    graph[g(i, j, 1)].append(g(i, j, 0))
                    graph[g(i, j, 2)].append(g(i, j, 3))
                    graph[g(i, j, 3)].append(g(i, j, 2))
                if shape[i][j] != 'l':
                    graph[g(i, j, 0)].append(g(i, j, 3))
                    graph[g(i, j, 3)].append(g(i, j, 0))
                    graph[g(i, j, 1)].append(g(i, j, 2))
                    graph[g(i, j, 2)].append(g(i, j, 1))
        # 步骤II：判断初始有水的位置
        djs = DisjointSet(total)
        water = set()
        for u in range(total):
            for v in graph[u]:
                djs.add(u, v)
            if u in up or u in down or u in left or u in right:
                djs.add(u, total) # 虚结点编号为total，对应边界外部
        for u in range(total):
            if djs.query(u, total):
                water.add(u)
        # 步骤III：逐高度层处理，判断与外界的连通性
        ans = 0
        djs = DisjointSet(total)
        for i in range(m - 1, -1, -1): # 从下到上处理
            for j in range(n):
                for d in range(4):
                    u = g(i, j, d)
                    for v in graph[u]:
                        if v != g(i - 1, j, 1):
                            djs.add(u, v)
                    if u in left or u in right or u in down:
                        djs.add(u, total)
            for j in range(n):
                for d in range(4):
                    u = g(i, j, d)
                    if not djs.query(u, total) and u in water: # 初始有水 and 没流出去 => 最终有水
                        ans += 1
        return ans // 2 # 每个方格蓄水量为2，每个方格的1/4的蓄水量是0.5，因此最终需要除以2


作者：Minori
链接：https://leetcode.cn/problems/kskhHQ/solution/by-minori-94tx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。