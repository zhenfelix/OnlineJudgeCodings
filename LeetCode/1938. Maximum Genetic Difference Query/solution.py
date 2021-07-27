class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        N = 20
        maxn = (1<<N)
        tree = [0]*maxn
        g = defaultdict(list)
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i 
            else:
                g[p].append(i)

        mp = defaultdict(list)
        for i, (idx, val) in enumerate(queries):
            mp[idx].append(i)
        ans = [0]*len(queries)

        def add(x):
            cur = 0
            tree[cur] += 1
            for i in range(N-1)[::-1]:
                delta = (x>>i)&1
                cur = cur*2 + delta + 1
                tree[cur] += 1

        def remove(x):
            cur = 0 
            tree[cur] -= 1
            for i in range(N-1)[::-1]:
                delta = (x>>i)&1
                cur = cur*2 + delta + 1
                tree[cur] -= 1

        def dfs(x):
            add(x)
            for i in mp[x]:
                _, val = queries[i]
                cur, res = 0, 0
                for bit in range(N-1)[::-1]:
                    delta = (val>>bit)&1
                    if tree[cur*2+2-delta]:
                        res += (1<<bit)
                        cur = cur*2 + 2 - delta
                    else:
                        cur = cur*2 + delta + 1
                ans[i] = res 
            for y in g[x]:
                dfs(y)
            remove(x)
            return

        dfs(root)
        return ans 