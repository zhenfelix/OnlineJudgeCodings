class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        res = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    r = i
                    while r < n:
                        if land[r][j] == 0:
                            break
                        c = j
                        while c < m:
                            if land[r][c] == 0:
                                break
                            land[r][c] = 0
                            c += 1
                        r += 1
                    res.append([i,j,r-1,c-1])
        return res
                    