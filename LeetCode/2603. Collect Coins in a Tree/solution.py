class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图
            deg[x] += 1
            deg[y] += 1

        # 用拓扑排序「剪枝」：去掉没有金币的子树
        q = deque()
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:  # 无金币叶子
                q.append(i)
        while q:
            for y in g[q.popleft()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        # 再次拓扑排序
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:  # 有金币叶子
                q.append(i)
        if len(q) <= 1:  # 至多一个有金币的叶子，直接收集
            return 0
        time = [0] * n
        while q:
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    time[y] = time[x] + 1  # 记录入队时间
                    q.append(y)

        # 统计答案
        return sum(time[x] >= 2 and time[y] >= 2 for x, y in edges) * 2


作者：endlesscheng
链接：https://leetcode.cn/problems/collect-coins-in-a-tree/solution/tuo-bu-pai-xu-ji-lu-ru-dui-shi-jian-pyth-6uli/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        cc = [[0]*4 for _ in range(n)]
        g = defaultdict(list)
        tot = sum(coins)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        dp = [0]*n 
        def dfs(cur, parent):
            if coins[cur] == 1:
                cc[cur][0] += 1
                cc[cur][-1] += 1
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(nxt,cur)
                cc[cur][1] += cc[nxt][0]
                cc[cur][2] += cc[nxt][1]
                cc[cur][3] += cc[nxt][3]
                if cc[nxt][3] == cc[nxt][0]+cc[nxt][1]:
                    continue
                dp[cur] += 2+dp[nxt]
            return 
        dfs(0,0) 
        # print(cc)
        # print(dp)
        ans = inf 
        def traverse(cur,parent,up,uc):
            nonlocal ans 
            cc[cur][1] += uc
            if tot == cc[cur][3]+cc[parent][1]+coins[parent]-coins[cur]:
                ans = min(ans, dp[cur])
            else:
                ans = min(ans,dp[cur]+up)
            # print(cur,dp[cur],up)
            for nxt in g[cur]:
                if nxt == parent: continue
                if cc[nxt][3] == cc[nxt][0]+cc[nxt][1]:
                    traverse(nxt,cur,dp[cur]+up+2,coins[cur])
                else:
                    traverse(nxt,cur,dp[cur]-dp[nxt]+up,coins[cur])
            return
        traverse(0,0,0,0)
        return ans 
