# class Solution:
#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
#         dist = []
#         for i, worker in enumerate(workers):
#             for j, bike in enumerate(bikes):
#                 dist.append((abs(worker[0]-bike[0])+abs(worker[1]-bike[1]),i,j))
#         worker_set, bike_set = set(), set()
#         n = len(workers)
#         ans = [-1]*n
#         heapq.heapify(dist)
#         while len(worker_set) < n:
#             _, i, j = heapq.heappop(dist)
#             if i in worker_set or j in bike_set:
#                 continue
#             worker_set.add(i)
#             bike_set.add(j)
#             ans[i] = j
#         return ans


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist.append((abs(worker[0]-bike[0])+abs(worker[1]-bike[1]),i,j))
        worker_set, bike_set = set(), set()
        n = len(workers)
        ans = [-1]*n
        dist.sort()
        for _, i, j in dist:
            if i in worker_set or j in bike_set:
                continue
            worker_set.add(i)
            bike_set.add(j)
            ans[i] = j
            if len(worker_set) >= n:
                break
        return ans
