class Solution:

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        n = len(edges) + 1

        g = [[] for _ in range(n)]

        for x, y in edges:

            g[x].append(y)

            g[y].append(x)  # 建树



        bob_time = [n] * n  # bobTime[x] 表示 bob 访问节点 x 的时间

        def dfs_bob(x: int, fa: int, t: int) -> bool:

            if x == 0:

                bob_time[x] = t

                return True

            found0 = False

            for y in g[x]:

                if y != fa and dfs_bob(y, x, t + 1):

                    found0 = True

            if found0:

                bob_time[x] = t  # 只有可以到达 0 才标记访问时间

            return found0

        dfs_bob(bob, -1, 0)



        g[0].append(-1)  # 防止把根节点当作叶子

        ans = -inf

        def dfs_alice(x: int, fa: int, alice_time: int, tot: int) -> None:

            if alice_time < bob_time[x]:

                tot += amount[x]

            elif alice_time == bob_time[x]:

                tot += amount[x] // 2

            if len(g[x]) == 1:  # 叶子

                nonlocal ans

                ans = max(ans, tot)  # 更新答案

                return

            for y in g[x]:

                if y != fa:

                    dfs_alice(y, x, alice_time + 1, tot)

        dfs_alice(0, -1, 0, 0)

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/most-profitable-path-in-a-tree/solutions/1964916/liang-bian-dfs-by-endlesscheng-da7j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)+1
        mark = [inf]*n 
        mark[bob] = 0
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs1(cur,parent):
            if cur == bob:
                return 0
            dist = inf 
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                nd = dfs1(nxt, cur)
                if nd < inf:
                    dist = nd+1
                    mark[cur] = dist
                    return dist
            return dist

        ans = -inf
        def dfs2(cur,parent,d,s):
            nonlocal ans 
            v = amount[cur]
            if d == mark[cur]:
                v //= 2  
            elif d > mark[cur]:
                v = 0 
            s += v
            child = 0
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs2(nxt,cur,d+1,s)
                child += 1 
            if child == 0:
                ans = max(ans, s)
            return
        dfs1(0,0)
        dfs2(0,0,0,0)
        return ans