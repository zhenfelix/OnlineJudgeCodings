class Solution:
    # def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    #     n, m = len(intervals), len(queries)
    #     ans = [-1]*m 
    #     # intervals = [[a, b, i] for i, (a, b) in enumerate(intervals)]
    #     queries = [[q, i] for i, q in enumerate(queries)]
    #     heapq.heapify(intervals)
    #     queries.sort()
    #     candidates = []
    #     for q, i in queries:
    #         while intervals and intervals[0][0] <= q:
    #             a, b = heapq.heappop(intervals)
    #             heapq.heappush(candidates, (b-a+1, b))
    #         while candidates and candidates[0][1] < q:
    #             heapq.heappop(candidates)
    #         if candidates:
    #             ans[i] = candidates[0][0]
    #     return ans 
    
    def minInterval(self, A, queries):
        A = sorted(A)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]