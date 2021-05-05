class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        g = defaultdict(list)
        for u, v, dis in paths:
            g[u].append((v,dis))
            g[v].append((u,dis))
        dp = {}
        dp[start,0] = 0
        q = []
        heapq.heappush(q,(0, start, 0))
        while q:
            cost, cur, cap = heapq.heappop(q)
            # print(cost, cur, cap)
            if cost > dp[cur,cap]:
                continue
            if cur == end:
                return dp[cur,cap]
            if cap < cnt and cost+charge[cur] < dp.get((cur,cap+1), float("inf")):
                dp[cur,cap+1] = cost+charge[cur]
                heapq.heappush(q,(cost+charge[cur],cur,cap+1))
            for nxt, dis in g[cur]:
                if dis <= cap and cost+dis < dp.get((nxt,cap-dis), float("inf")):
                    dp[nxt,cap-dis] = cost+dis 
                    heapq.heappush(q,(cost+dis,nxt,cap-dis))
        return -1

