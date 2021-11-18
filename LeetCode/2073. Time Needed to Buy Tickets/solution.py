# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         q = deque([(i,t) for i, t in enumerate(tickets)])
#         cur = 0
#         while q:
#             cur += 1
#             i, t = q.popleft()
#             t -= 1
#             if i == k and t == 0:
#                 return cur
#             if t > 0:
#                 q.append((i,t))
#         return -1

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(t,tickets[k]) if i <= k else min(t,tickets[k]-1) for i, t in enumerate(tickets))