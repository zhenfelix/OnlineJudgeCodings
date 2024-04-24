class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (x, y, w) in enumerate(edges):
            g[x].append((y, w, i))
            g[y].append((x, w, i))

        # Dijkstra 算法模板
        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, w, _ in g[x]:
                new_dis = dx + w
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    heappush(h, (new_dis, y))

        ans = [False] * len(edges)
        # 图不连通
        if dis[-1] == inf:
            return ans

        # 从终点出发 BFS
        vis = [False] * n
        vis[-1] = True
        q = deque([n - 1])
        while q:
            y = q.popleft()
            for x, w, i in g[y]:
                if dis[x] + w != dis[y]:
                    continue
                ans[i] = True
                if not vis[x]:
                    vis[x] = True
                    q.append(x)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-edges-in-shortest-paths/solutions/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。