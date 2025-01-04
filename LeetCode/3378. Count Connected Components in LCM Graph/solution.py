nmax = 2*10**5+10
factors = defaultdict(list)
for f in range(1,nmax+1):
    for v in range(f,nmax+1,f):
        factors[v].append(f)

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        nums = sorted(nums)
        mp = dict()
        for i, v in enumerate(nums):
            mp[v] = i 
        n = len(nums)
        parent = list(range(n))
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv 
            return
        gs = defaultdict(list)
        for v in sorted(nums):
            for f in factors[v]:
                gs[f].append(v)
        for f, vs in gs.items():
            if f > threshold: break
            for v in vs:
                if v*vs[0] > threshold*f: break
                connect(mp[v],mp[vs[0]])


        return len(set([find(i) for i in range(n)]))




class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        fa = list(range(n))
        # 非递归并查集
        def find(x: int) -> int:
            rt = x
            while fa[rt] != rt:
                rt = fa[rt]
            while fa[x] != rt:
                fa[x], x = rt, fa[x]
            return rt

        # 记录每个数的下标
        idx = {x: i for i, x in enumerate(nums)}

        for g in range(1, threshold + 1):
            fi = -1
            for x in range(g, threshold + 1, g):
                if x in idx:
                    fi = find(idx[x])
                    break
            if fi < 0:
                continue
            for y in range(x + g, g * threshold // x + 1, g):
                if y in idx:
                    fj = find(idx[y])
                    if fj != fi:
                        fa[fj] = fi  # 合并 idx[x] 和 idx[y]
                        n -= 1  # 连通块个数减一
        return n

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-connected-components-in-lcm-graph/solutions/3013720/mei-ju-gcd-bing-cha-ji-pythonjavacgo-by-sq6vd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。