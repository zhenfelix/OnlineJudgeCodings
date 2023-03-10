# class Solution:
#     def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
#         n, m = len(grid), len(grid[0])
#         def dfs(r,c):
#             if (r,c) == (n-1,m-1):
#                 return True
#             if 0 <= r < n and 0 <= c < m:
#                 if grid[r][c] == 0: return False
#                 grid[r][c] = 0
#                 if dfs(r+1,c) or dfs(r,c+1):
#                     return True 
#             return False
#         dfs(0,0)
#         grid[0][0] = grid[-1][-1] = 1
#         def dfs2(r,c):
#             if (r,c) == (n-1,m-1):
#                 return True
#             if 0 <= r < n and 0 <= c < m:
#                 if grid[r][c] == 0: return False
#                 grid[r][c] = 0
#                 if dfs(r,c+1) or dfs(r+1,c):
#                     return True 
#             return False
#         return not dfs2(0,0)  

class Solution:
    def isPossibleToCutPath(self, g: List[List[int]]) -> bool:
        m, n = len(g), len(g[0])
        def dfs(x: int, y: int) -> bool:  # 返回能否到达终点
            if x == m - 1 and y == n - 1: return True
            g[x][y] = 0  # 直接修改
            return x < m - 1 and g[x + 1][y] and dfs(x + 1, y) or \
                   y < n - 1 and g[x][y + 1] and dfs(x, y + 1)
        return not dfs(0, 0) or not dfs(0, 0)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/solution/zhuan-huan-cheng-qiu-lun-kuo-shi-fou-xia-io8x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。