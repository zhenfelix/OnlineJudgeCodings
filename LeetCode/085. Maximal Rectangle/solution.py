from __future__ import annotations
from pprint import pprint

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n==0:
            return 0
        m = len(matrix[0])
        left = [0]*m
        right = [m]*m
        height = [0]*m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    height[j] = height[j]+1
                else:
                    height[j] = 0
                    
            cur_left = 0
            for j in range(m):
                if matrix[i][j]=='1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
                    
            cur_right = m
            for j in range(m-1,-1,-1):
                if matrix[i][j]=='1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = m
                    cur_right = j
                    
            for j in range(m):
                ans = max(ans, (right[j]-left[j])*height[j])

            pprint(left)
            pprint(right)
            pprint(height)
            print('\n')
        
        return ans


s = Solution()
mat = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]
pprint(mat)
s.maximalRectangle(mat)