class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(cur,pre):
            cnt = 0
            for nxt in g[cur]:
                if nxt == pre: continue
                cnt += dfs(nxt,cur)
                values[cur] += values[nxt]
            values[cur] %= k 
            if values[cur] == 0:
                cnt += 1
            return cnt
        return dfs(0,0)



class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        path = [[] for _ in range(n)]
        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
        tmp = [0] * n
        def dfs(u, p = -1):
            ans = values[u]
            for v in path[u]:
                if v != p:
                    dfs(v, u)
                    ans += tmp[v]
            tmp[u] = ans % k
        dfs(0)
        return tmp.count(0)


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/slLdgm/view/ytByYQ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。