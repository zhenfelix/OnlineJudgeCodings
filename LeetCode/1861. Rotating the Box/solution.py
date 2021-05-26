class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        cnt = [[0]*n for _ in range(m)]
        res = [["."]*n for _ in range(m)]
        # for i in range(n):
        #     for j in range(m):
        #         res[j][i] = box[i][j]

        for j in range(n)[::-1]:
            bottom = m
            for i in range(m)[::-1]:
                if box[j][i] == "*":
                    res[i][n-1-j] = "*"
                    bottom = i 
                elif box[j][i] == "#":
                    bottom -= 1
                    res[bottom][n-1-j] = "#"
        return res
