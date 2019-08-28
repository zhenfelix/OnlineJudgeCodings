# import heapq

# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         j = 1
#         arr = [(i*j, i, j) for i in range(1,m+1,1)]
#         heapq.heapify(arr)
#         for _ in range(k):
#             res, i, j = heapq.heappop(arr)
#             if j + 1 <= n:
#                 heapq.heappush(arr,(i*(j+1), i, j+1))
#         return res
        
    
# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         def binary_search(func_array, left, right, func_condition, **kwargs):
#             while left <= right:
#                 mid = (left+right)//2
#                 if func_condition(func_array(mid), kwargs['arg_condition']):
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return left
        
#         def less_than(target, var):
#             i, j = var[0], var[1]
#             cc = 0
#             while i <= m and j >= 1:
#                 if i*j >= target:
#                     j = binary_search(lambda x: i*x, 1, j, lambda x, y: x >= y, arg_condition = target) - 1
#                 else:
#                     new_i = binary_search(lambda x: x*j, i, m, lambda x, y: x >= y, arg_condition = target)
#                     cc += (new_i - i)*j
#                     i = new_i
#                     if cc >= k:
#                         return True
#             return False
        
#         return binary_search(lambda x: x, 1, m*n, less_than, arg_condition = (1,n)) - 1

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def less_than(target):
            cc = 0
            for i in range(1,m+1,1):
                cc += min(n,(target-1)//i)
                
            return cc >= k
                    
        lo, hi = 1, m*n
        while lo <= hi:
            x = (lo+hi)//2
            if less_than(x):
                hi = x - 1
            else:
                lo = x + 1
        return hi


                
        