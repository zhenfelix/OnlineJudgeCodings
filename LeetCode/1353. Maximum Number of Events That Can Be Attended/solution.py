class Solution:
    # def maxEvents(self, events: List[List[int]]) -> int:
    #     res, cur = 0, -float('inf')
    #     q = [(a,b) for a,b in events]
    #     heapq.heapify(q)
    #     while q:
    #         a, b = heapq.heappop(q)
    #         if b < cur:
    #             continue
    #         if a < cur:
    #             heapq.heappush(q,(cur,b))
    #         else:
    #             cur = a + 1
    #             res += 1
    #     return res
    
    def maxEvents(self, A):
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res