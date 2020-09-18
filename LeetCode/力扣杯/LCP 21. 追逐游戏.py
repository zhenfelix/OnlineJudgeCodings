class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        def dfs(cur, parent):
            if cur in visited:
                return [cur]
            st.append(cur)
            visited.add(cur)
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                nodes = dfs(nxt, cur)
                if nodes:
                    return nodes
            st.pop()
            return []


        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        st, visited = [], set()
        mark = dfs(startB, -1)
        n = len(edges)
        # print(mark)
        cycle = set()
        while st:
            cur = st.pop()
            cycle.add(cur)
            if cur == mark[0]:
                break
        # print(cycle)
        def dist(cur, parent, step):
            if cur in cycle:
                return step, cur
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                tmp = dist(nxt, cur, step+1)
                if tmp:
                    return tmp
            return None

        # def dist2(cur, parent, step):
        #     res = step
        #     for nxt in g[cur]:
        #         if nxt == parent or nxt in cycle:
        #             continue
        #         res = max(res, dist2(nxt,cur,step+1))
        #     return res 

        def measure(cur, parent, step, target):
            if cur == target:
                return step
            res = float('inf')
            for nxt in g[cur]:
                if nxt == parent or nxt not in cycle:
                    continue
                res = min(res, measure(nxt, cur, step+1, target))
            return res

        cycleDistA, cycleA = dist(startA,-1,0)
        cycleDistB, cycleB = dist(startB,-1,0)
        # print(cycleDistA, cycleA)
        # print(cycleDistB, cycleB)
        ss = measure(cycleA,-1,0,cycleB)
        # print(ss)

        def bfs(cur,arr):
            q = deque()
            q.append((cur,0))
            arr[cur] = 0
            while q:
                cur, dd = q.pop()
                for nxt in g[cur]:
                    if dd+1 < arr[nxt]:
                        arr[nxt] = dd + 1
                        q.append((nxt,dd+1))
            return

        A, B = [float('inf')]*(n+1), [float('inf')]*(n+1)
        bfs(startA,A)
        bfs(startB,B)

        if len(cycle) >= 4 and cycleDistA + ss > cycleDistB + 1:
                return -1
        res = 1
        for i in range(1,n+1):
            if A[i] > B[i] + 1:
                res = max(res, A[i])

        return res
