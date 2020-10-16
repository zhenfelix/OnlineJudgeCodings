class Solution:
    # def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
    #     units = []
    #     maxq = []
    #     sums, res = 0, float('inf')
    #     for i, (q,w) in enumerate(zip(quality,wage)):
    #         units.append((w/q,i))
    #     units.sort()
    #     for price, i in units:
    #         if len(maxq) == K:
    #             q = heapq.heappop(maxq)
    #             sums += q 
    #         heapq.heappush(maxq, -quality[i])
    #         sums += quality[i]
    #         if len(maxq) == K:
    #             res = min(res,price*sums)
    #     return res

    
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res
    
# FAQ:
# Question: "However, it is possible that current worker has the highest quality, so you removed his quality in the last step, which leads to the problem that you are "using his ratio without him".
# Answer: It doesn't matter. The same group will be calculated earlier with smaller ratio.
# And it doesn't obey my logic here: For a given ratio of wage/quality, find minimum total wage of K workers.