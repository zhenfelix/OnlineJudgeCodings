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