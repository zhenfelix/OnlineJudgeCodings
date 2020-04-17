# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         def find_rgt(left, right, row):
#             while left <= right:
#                 mid = (left+right)//2
#                 # print(left,right,row)
#                 if grid[row][mid] < 0:
#                     right = mid-1
#                 else:
#                     left = mid+1
#             return left
        
#         res = 0
#         m, n = len(grid), len(grid[0])
#         start, end = 0, n-1
#         for r in range(m):
#             idx = find_rgt(start,end,r)
#             res += n-idx
#             # end = idx
#         return res
            
    
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cur, res = n-1, 0
        for r in range(m):
            while cur >= 0 and grid[r][cur] < 0:
                cur -= 1
            res += n-cur-1
        return res
            