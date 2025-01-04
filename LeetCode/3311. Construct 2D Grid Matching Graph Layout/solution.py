class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 找一个度数最小的点
        x = 0
        for i, to in enumerate(g):
            if len(to) < len(g[x]):
                x = i

        row = [x]
        vis = [False] * n
        vis[x] = True
        deg_st = len(g[x])  # 起点的度数
        while True:  # 注意题目保证 n >= 2，可以至少循环一次
            nxt = -1
            for y in g[x]:
                if not vis[y] and (nxt < 0 or len(g[y]) < len(g[nxt])):
                    nxt = y
            x = nxt
            row.append(x)
            vis[x] = True
            if len(g[x]) == deg_st:
                break

        ans = [[] for _ in range(n // len(row))]
        ans[0] = row
        for i in range(1, len(ans)):
            for x in ans[i - 1]:
                for y in g[x]:
                    # x 上左右的邻居都访问过了，没访问过的邻居只会在 x 下面
                    if not vis[y]:
                        vis[y] = True
                        ans[i].append(y)
                        break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/solutions/2940537/fen-lei-tao-lun-zhu-xing-gou-zao-by-endl-v3x0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。