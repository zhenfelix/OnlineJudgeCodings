# import heapq

# class Solution:
#     def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
#         heap_cap, heap_pro = list(zip(Capital,Profits)), []
#         heapq.heapify(heap_cap)
#         for i in range(k):
#             while  heap_cap and heap_cap[0][0] <= W:
#                 c, p = heapq.heappop(heap_cap)
#                 heapq.heappush(heap_pro,-p)

#             if heap_pro:
#                 p = heapq.heappop(heap_pro)
#                 W += -p 
#             else:
#                 break
#         return W
    
    
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        n = len(Profits)
        projects = list(zip(Capital, Profits))
        projects.sort(key=lambda a: a[0])
        pq = []
        
        j = 0
        ans = W
        for i in range(min(k, n)):
             while j < n and projects[j][0] <= ans:
                heapq.heappush(pq, -projects[j][1])
                j += 1
             if pq:
                ans -= heapq.heappop(pq)
        return ans