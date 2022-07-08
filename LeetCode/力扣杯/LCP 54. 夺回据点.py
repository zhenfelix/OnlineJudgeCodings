class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        n = len(cost)
        g = defaultdict(list)
        components = []
        iscut = [False]*n 
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        # print(g)
        rank = [-1]*n 
        lo = [-1]*n 
        st = []
        timer = 0
        def tarjan(cur, pre):
            nonlocal timer
            timer += 1
            rank[cur] = timer
            lo[cur] = timer
            st.append(cur)
            child = 0
            for nxt in g[cur]:
                if rank[nxt] == -1:
                    tarjan(nxt, cur)
                    lo[cur] = min(lo[cur], lo[nxt])
                    # child += 1
                    if lo[nxt] >= rank[cur]:
                        child += 1
                        if child > 1 or cur != pre:
                            iscut[cur] = True
                        components.append([])
                        # print(cur,nxt)
                        while True:
                            components[-1].append(st.pop())
                            if components[-1][-1] == nxt:
                                break
                        components[-1].append(cur)
                else:
                    lo[cur] = min(lo[cur], rank[nxt])
            return

        tarjan(0, 0)
        # print(components)
        # print(rank,iscut)
        if len(components) == 1:
            return min(cost[i] for i in components[-1])
        mn = []
        for component in components:
            cnt, tmp = 0, float('inf')
            for c in component:
                if iscut[c]:
                    cnt += 1
                else:
                    tmp = min(tmp, cost[c])
            if cnt == 1:
                mn.append(tmp)
        # print(mn)
        return sum(mn)-max(mn)