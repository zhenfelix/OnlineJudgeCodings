class Solution:
#     def maximumScore(self, a, b, c):
#         return min((a + b + c) // 2, a + b + c - max(a, b, c))
        
    
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        c = min(a+b, c)
        return (a + b + c) >> 1
    
    
# class Solution:
#     def maximumScore(self, a: int, b: int, c: int) -> int:
#         q = [-a,-b,-c]
#         heapq.heapify(q)
#         cnt = 0
#         while len(q) >= 2:
#             a = -heapq.heappop(q)
#             b = -heapq.heappop(q)
#             a -= 1
#             if a:
#                 heapq.heappush(q,-a)
#             b -= 1
#             if b:
#                 heapq.heappush(q,-b)
#             cnt += 1
#         return cnt