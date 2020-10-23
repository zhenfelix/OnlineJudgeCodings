class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def calc(x,y):
            total, epsilon = 0, 0.000005
            for r,c,q in towers:
                d = ((r-x)**2 + (c-y)**2)**0.5
                if d <= radius + epsilon:
                    total += q//(1+d)
            return total
        res, ii, jj = 0, -1, -1
        for i in range(51):
            for j in range(51):
                cur = calc(i,j)
                if cur > res:
                    res, ii, jj = cur, i, j 
        return [ii,jj]