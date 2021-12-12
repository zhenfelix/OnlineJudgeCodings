import sys

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        sys.setrecursionlimit(10**6)

        g = defaultdict(list)
        degree = defaultdict(int)
        for i, (s,e) in enumerate(pairs):
            g[s].append(i)
            degree[s] += 1
            degree[e] -= 1
        start, end = -1, -1
        for k, v in degree.items():
            if v == 1:
                start = k
            if v == -1:
                end = k

        # print(g,start,end)
        if start == -1:
            start = pairs[0][0]
        res = []

        def dfs(cur, res):
            while g[cur]:
                idx = g[cur].pop()
                s, e = pairs[idx]
                dfs(e, res)
                res.append(idx)   
            return
        dfs(start, res)
        return [pairs[idx] for idx in res[::-1]]
