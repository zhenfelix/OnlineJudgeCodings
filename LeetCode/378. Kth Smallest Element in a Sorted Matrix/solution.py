# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         def search(i,j,target):
#             cc = 0
#             while i < n and j >= 0:
#                 # print(i,j)
#                 if matrix[i][j] >= target:
#                     j -= 1
#                 else:
#                     # print("i: ", i)
#                     cc += j + 1
#                     i += 1
#             return cc
#         left, right = matrix[0][0], matrix[-1][-1]
#         while left <= right:
#             mid = (left+right)//2
#             if search(0,n-1,mid) >= k:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         # print(search(0,n-1,15))
#         return right

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         def search(i,j,target):
#             cc = 0
#             while i < n and j >= 0:
#                 # print(i,j)
#                 if matrix[i][j] >= target:
#                     # j -= 1
#                     lo, hi = 0, j
#                     while lo <= hi:
#                         mid = (lo+hi)//2
#                         if matrix[i][mid] >= target:
#                             hi = mid - 1
#                         else:
#                             lo = mid + 1
#                     j = hi
#                 else:
#                     # print("i: ", i)
#                     lo, hi = i, n-1
#                     while lo <= hi:
#                         mid = (lo+hi)//2
#                         if matrix[mid][j] < target:
#                             lo = mid + 1
#                         else:
#                             hi = mid - 1
                    
#                     cc += (j + 1)*(lo - i)
#                     i = lo
#                     if cc >= k:
#                         return True
#             return False
        
#         left, right = matrix[0][0], matrix[-1][-1]
#         while left <= right:
#             mid = (left+right)//2
#             if search(0,n-1,mid):
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         # print(search(0,n-1,15))
#         return right


# import random

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def binary_search(func_array, left, right, func_half, **kwargs):
            while left <= right:
                mid = (left + right)//2
                # mid = random.randint(left,right)
                if func_half(func_array(mid), kwargs['var_half']):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        def less_than(target, mat):
            i, j, n = 0, len(mat)-1, len(mat)
            cc = 0
            while i < n and j >= 0:
                if mat[i][j] >= target:
                    j = binary_search(lambda x: mat[i][x], 0, j-1, lambda x, y: x >= y, var_half = target) - 1
                else:
                    new_i = binary_search(lambda x: mat[x][j], i, n-1, lambda x, y: x >= y, var_half = target)
                    cc += (new_i - i)*(j + 1)
                    i = new_i
                    if cc >= k:
                        return True
            return False
        
        idx = binary_search(lambda x: x, matrix[0][0], matrix[-1][-1], less_than, var_half = matrix) - 1
        return idx
            
            
# import heapq

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         arr = [(matrix[i][0], i, 0) for i in range(n)]
#         heapq.heapify(arr)
        
#         num, row = -1, -1
#         for _ in range(k):
#             num, row, col = heapq.heappop(arr)
#             if col + 1 < n:
#                 heapq.heappush(arr, (matrix[row][col+1], row, col+1))
#         return num
        