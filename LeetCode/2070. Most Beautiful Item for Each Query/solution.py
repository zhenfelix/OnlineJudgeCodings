class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m = len(queries)
        res = [0]*m 
        qs = [(q,i) for i, q in enumerate(queries)]
        qs.sort()
        hq = [(-b,p) for p,b in items]
        heapq.heapify(hq)
        for q, i in qs[::-1]:
            while hq and hq[0][-1] > q:
                heapq.heappop(hq)
            if hq:
                res[i] = -hq[0][0]
        return res 