# from collections import Counter
# import heapq

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         mp = Counter(tasks)
#         arr = [(-a[1],a[0]) for a in mp.items()]
#         heapq.heapify(arr)
#         res = 0
#         while arr:
#             tmp = []
#             for i in range(n+1):
#                 if arr:
#                     front = heapq.heappop(arr)
#                     res += 1
#                 else:
#                     if tmp:
#                         res += 1
#                         continue
#                     else:
#                         return res
                
#                 if front[0] < -1:
#                     tmp.append((front[0]+1,front[1]))
#             for cnt, ch in tmp:
#                 heapq.heappush(arr,(cnt,ch))
#         return res

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        
        cc, maxres = 0, -float('inf')
        # arr = sorted(mp.items, lambda x: x[1])
        for k, v in mp.items():
            if v == maxres:
                cc += 1
            elif v > maxres:
                maxres = v
                cc = 1
        return max(len(tasks),(maxres-1)*(n+1)+cc)