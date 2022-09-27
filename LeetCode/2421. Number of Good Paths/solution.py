class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        # 并查集模板
        fa = list(range(n))
        # size[x] 表示节点值等于 vals[x] 的节点个数，如果按照节点值从小到大合并，size[x] 也是连通块内的等于最大节点值的节点个数
        size = [1] * n
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = n
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)
            for y in g[x]:
                y = find(y)
                if y == fx or vals[y] > vx: continue  # 只考虑最大节点值比 vx 小的连通块
                if vals[y] == vx:  # 可以构成好路径
                    ans += size[fx] * size[y]  # 乘法原理
                    size[fx] += size[y]  # 统计连通块内节点值等于 vx 的节点个数
                fa[y] = fx  # 把小的节点值合并到大的节点值上
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/number-of-good-paths/solution/bing-cha-ji-by-endlesscheng-tbz8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        parent = [i for i in range(n)]
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        mp = defaultdict(list)
        ans = 0
        arr = set()
        for i, v in enumerate(vals):
            mp[v].append(i)
            arr.add(v)
        arr = sorted(list(arr))
        hq = []
        edges.sort(key = lambda x: max(vals[x[0]], vals[x[1]]))
        cur = 0
        for v in arr:
            ans += len(mp[v])
            while cur < n-1 and max(vals[edges[cur][0]],vals[edges[cur][1]]) <= v:
                a, b = edges[cur]
                connect(a,b)
                cur += 1
            gs = mp[v]
            cc = Counter([find(i) for i in gs])
            for pi, cnt in cc.items():
                ans += cnt*(cnt-1)//2
        return ans



class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        parent = [i for i in range(n)]
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        mp = defaultdict(list)
        ans = 0
        arr = set()
        for i, v in enumerate(vals):
            mp[v].append(i)
            arr.add(v)
        arr = sorted(list(arr))
        hq = []
        edges.sort(key = lambda x: (vals[x[0]], vals[x[1]]))
        cur = 0
        for v in arr:
            ans += len(mp[v])
            while cur < n-1 and vals[edges[cur][0]] <= v:
                heappush(hq, (vals[edges[cur][1]], edges[cur][0], edges[cur][1]))
                cur += 1
            while hq and hq[0][0] <= v:
                _, a, b = heappop(hq)
                connect(a,b)
            gs = mp[v]
            cc = Counter([find(i) for i in gs])
            for pi, cnt in cc.items():
                ans += cnt*(cnt-1)//2
        return ans
