class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        def dfs1(u):
            vis[u] = True
            for v in g[u]:
                if vis[v] == False:
                    dfs1(v)
            s.append(u)

        def dfs2(u):
            nonlocal sccCnt
            color[u] = sccCnt
            for v in g2[u]:
                if color[v] == False:
                    dfs2(v)

        sccCnt = 0
        n = len(edges)
        g = defaultdict(list)
        g2 = defaultdict(list)
        color = [0]*n 
        vis = [0]*n 
        s = []
        for a, b in enumerate(edges):
            g[a].append(b)
            g2[b].append(a)
        for i in range(n):
            if vis[i] == False:
                dfs1(i)
        for i in range(n)[::-1]:
            if color[s[i]] == False:
                sccCnt = sccCnt + 1
                dfs2(s[i])
        dp = [0]*(sccCnt+1)
        rg = defaultdict(set)
        degree = [0]*(sccCnt+1)
        sz = [0]*(sccCnt+1)
        for i in range(n):
            sz[color[i]] += 1
        for a, b in enumerate(edges):
            if color[a] == color[b]: continue
            rg[color[b]].add(color[a])
            degree[color[a]] += 1
        # print(color,sz,degree)
        q = deque()
        for i in range(sccCnt):
            if degree[i+1] == 0:
                q.append(i+1)
        while q:
            cur = q.popleft()
            dp[cur] += sz[cur]
            for nxt in rg[cur]:
                dp[nxt] += dp[cur]
                degree[nxt] -= 1 
                if degree[nxt] == 0:
                    q.append(nxt)
        # print(dp)

        return [dp[color[i]] for i in range(n)]


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [-1] * n
        vis = [0] * n
        for i in range(n):
            if ans[i] == -1:
                tmp = []
                pt = i
                while not vis[pt]:
                    vis[pt] = 1
                    tmp.append(pt)
                    pt = edges[pt]
                # 表示找到了新的环，先更新环上的所有点
                if ans[pt] == -1:
                    length = len(tmp) - tmp.index(pt)
                    # 对于环上的点更新答案，并只保留剩下不在环上的点
                    while True:
                        v = tmp.pop()
                        ans[v] = length
                        if v == pt: break
                v = ans[pt]
                while tmp:
                    v += 1
                    ans[tmp.pop()] = v
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/9idUqp/view/mTzR0t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def countVisitedNodes(self, g: List[int]) -> List[int]:
        n = len(g)
        rg = [[] for _ in range(n)]  # 反图
        deg = [0] * n
        for x, y in enumerate(g):
            rg[y].append(x)
            deg[y] += 1

        # 拓扑排序，剪掉 g 上的所有树枝
        # 拓扑排序后，deg 值为 1 的点必定在基环上，为 0 的点必定在树枝上
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = g[x]
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        ans = [0] * n
        # 在反图上遍历树枝
        def rdfs(x: int, depth: int) -> None:
            ans[x] = depth
            for y in rg[x]:
                if deg[y] == 0:  # 树枝上的点在拓扑排序后，入度均为 0
                    rdfs(y, depth + 1)
        for i, d in enumerate(deg):
            if d <= 0:
                continue
            ring = []
            x = i
            while True:
                deg[x] = -1  # 将基环上的点的入度标记为 -1，避免重复访问
                ring.append(x)  # 收集在基环上的点
                x = g[x]
                if x == i:
                    break
            for x in ring:
                rdfs(x, len(ring))  # 为方便计算，以 len(ring) 作为初始深度
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/9idUqp/view/QFZ1w1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。