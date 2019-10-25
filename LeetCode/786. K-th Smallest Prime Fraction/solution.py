import math

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        def less_than(target):
            i = j = 0
            cc = 0
            last, last_i, last_j = 0, -1, -1
            while i < n and j < n:
                if target > A[i]/A[j]:
                    if A[i]/A[j] > last:
                        last, last_i, last_j = A[i]/A[j], i, j
                    cc += n - j
                    i += 1
                else:
                    j += 1
            return cc, last_i, last_j
        
        lo, hi = A[0]/A[-1], 2
        while True:
            mid = math.sqrt(lo*hi)
            count, x, y = less_than(mid)
            if count == K:
                return [A[x],A[y]]
            elif count > K:
                hi = mid
            else:
                lo = mid
        return [-1,-1]

# import math

# class Solution:
#     def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        
#         n = len(A)
#         l, r = A[0]/A[-1], 1
#         p, q = 0, 1
        
#         while l < r:
#             m = math.sqrt(l * r)
#             p = 0
#             cnt, j = 0, n - 1
#             for i in range(n):
#                 while j >= 0 and A[i] > m*A[n-1-j]:
#                     j -= 1
#                 cnt += j + 1
#                 if j >= 0 and p * A[n-1-j] < q * A[i]:
#                     p, q = A[i], A[n-1-j]
#                     #print(p, q)
#             #print(m, cnt, p, q)        
#             if cnt < K:
#                 l = m
#             elif cnt > K:
#                 r = m
#             else:
#                 return [p, q]



# import heapq

# class Solution:
#     def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
#         n = len(A)
#         for i in range(n):
#             heap.append((A[i]/A[n-1], i, n-1))
#         heapq.heapify(heap)
#         p, q = -1, -1
#         for _ in range(K):
#             x, i, j = heapq.heappop(heap)
#             p, q = A[i], A[j]
#             if j > i + 1:
#                 heapq.heappush(heap,(A[i]/A[j-1], i, j-1))
#         return [p,q]



# class Solution:
#     def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
#         def countLess(target):
#             cnt, j, top, p, q = 0, n-1, -float('inf'), -1, -1
#             while j > 0 and target > A[0]/A[j]:
#                 j -= 1
#             j += 1
#             if j > n-1:
#                 return cnt, p, q
#             if A[0]/A[j] > top:
#                 top = A[0]/A[j]
#                 p, q = A[0], A[j]
#             cnt += n-j
#             for i in range(1,n-1):
#                 while j <= i:
#                     j += 1
#                 while j <= n-1 and A[i]/A[j] >= target:
#                     j += 1
#                 if j > n-1:
#                     break
#                 if A[i]/A[j] > top:
#                     top = A[i]/A[j]
#                     p, q = A[i], A[j]
#                 cnt += n-j
#             return cnt, p, q

#         lo, hi, n = 0, 1, len(A)
#         while lo < hi:
#             mid = (lo+hi)/2
#             cnt_, p_, q_ = countLess(mid)
#             if cnt_ == K:
#                 return [p_, q_]
#             elif cnt_ < K:
#                 lo = mid
#             else:
#                 hi = mid
#         return -1

