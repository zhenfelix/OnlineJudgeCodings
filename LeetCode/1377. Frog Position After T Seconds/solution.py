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




class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        dp = [0]*(n+1)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dp[1] = 1
        res = [0]

        def dfs(cur, parent, depth):
            tot = len([i for i in graph[cur] if i != parent])
            if cur == target:
                if depth == t:
                    res[0] = dp[cur]
                if depth < t and tot == 0:
                    res[0] = dp[cur]
                return
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                dp[nxt] = dp[cur]/tot
                dfs(nxt,cur,depth+1)
            return

        dfs(1,0,0)
        return res[0]

