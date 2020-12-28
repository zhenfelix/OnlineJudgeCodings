class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        q = []
        cnt = 0
        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(q,(i+days[i],apples[i]))
            while q and q[0][0] <= i:
                heapq.heappop(q)
            if q:
                t, cc = heapq.heappop(q)
                cnt += 1
                if cc > 1:
                    heapq.heappush(q,(t,cc-1))
        cur = n
        while q:
            t, cc = heapq.heappop(q)
            if t > cur:
                cnt += min(t-cur,cc)
                cur = min(t,cur+cc)
        return cnt 