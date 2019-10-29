# import heapq
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted([(d,p) for d,p in zip(difficulty,profit)])
        # heapq.heapify(jobs)
        # worker = sorted(worker)
        worker.sort()
        heap = []
        sums, idx, cur = 0, 0, 0
        for work in worker:
            while idx < len(jobs) and jobs[idx][0] <= work:
                # heapq.heappush(heap,-jobs[idx][-1])
                cur = max(cur,jobs[idx][-1])
                idx += 1
            sums += cur
        return sums