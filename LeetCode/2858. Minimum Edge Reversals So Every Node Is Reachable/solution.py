class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        seen = set()
        down = [0]*n 
        up = [0]*n 
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            seen.add((u,v))
        def dfs(cur,pre):
            for nxt in g[cur]:
                if nxt == pre: continue
                dfs(nxt,cur)
                delta = 1 if (cur,nxt) in seen else 0
                down[cur] += down[nxt]+delta
            return 
        def dfs2(cur,pre):
            for nxt in g[cur]:
                if nxt == pre: continue
                delta = 1 if (cur,nxt) in seen else 0
                up[nxt] = down[cur]-(down[nxt]+delta)+up[cur]
                up[nxt] += 1-delta
                dfs2(nxt,cur)
            return

        dfs(0,0)
        dfs2(0,0)
        # print(down,up)
        return [n-1-up[i]-down[i] for i in range(n)]


class Solution:

    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:

        g = [[] for _ in range(n)]

        for x, y in edges:

            g[x].append((y, 1))

            g[y].append((x, -1))  # 从 y 到 x 需要反向



        ans = [0] * n

        def dfs(x: int, fa: int) -> None:

            for y, dir in g[x]:

                if y != fa:

                    ans[0] += dir < 0

                    dfs(y, x)

        dfs(0, -1)



        def reroot(x: int, fa: int) -> None:

            for y, dir in g[x]:

                if y != fa:

                    ans[y] = ans[x] + dir  # dir 就是从 x 换到 y 的「变化量」

                    reroot(y, x)

        reroot(0, -1)

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-edge-reversals-so-every-node-is-reachable/solutions/2445681/mo-ban-huan-gen-dppythonjavacgojs-by-end-8qiu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。