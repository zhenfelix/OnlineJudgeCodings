class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row = [0]*n 
        col = [0]*m 
        mp = dict()
        for i in range(n):
            for j in range(m):
                mp[mat[i][j]] = (i,j)
        for i, v in enumerate(arr):
            x, y = mp[v]
            row[x] += 1
            col[y] += 1
            if row[x] == m or col[y] == n:
                return i 
        return -1