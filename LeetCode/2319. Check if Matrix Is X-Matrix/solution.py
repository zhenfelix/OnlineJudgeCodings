class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                a = grid[i][j]
                if i == j and a == 0:
                    return False
                if i+j == n-1 and a == 0:
                    return False
                if i != j and i+j != n-1 and a != 0:
                    return False
        return True