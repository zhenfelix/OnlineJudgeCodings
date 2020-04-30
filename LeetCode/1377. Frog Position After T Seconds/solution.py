class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        found = [False]

        def dfs(cur,prob,step,pre):
            # print(cur,prob,step,pre)
            if found[0]:
                return 0
            if step == 0:
                if cur == target:
                    found[0] = True
                    return prob
                return 0
            sz = len(g[cur]) - (pre != cur)
            if sz == 0:
                return prob if cur == target else 0
            sums = 0
            for nxt in g[cur]:
                if nxt != pre:
                    sums += dfs(nxt,prob/sz,step-1,cur)
            return sums
            
        return dfs(1,1,t,1)
