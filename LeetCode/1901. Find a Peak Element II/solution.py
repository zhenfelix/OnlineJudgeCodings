class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        i, j = 0, 0
        found = False
        dij = [0,-1,0,1,0]
        while not found:
            found = True
            for di, dj in zip(dij,dij[1:]):
                di += i 
                dj += j
                if di < 0 or di >= n or dj < 0 or dj >= m:
                    continue
                # print(di,dj)
                if mat[di][dj] > mat[i][j]:
                    found = False 
                    i, j = di, dj 
                    break
        return [i,j]

