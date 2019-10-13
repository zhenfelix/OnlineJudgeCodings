class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def crossProduct(u,v):
            return u[0]*v[1] - u[1]*v[0]

        n = len(points)
        vectors = [(points[i][0]-points[(i-1)%n][0],points[i][1]-points[(i-1)%n][1]) for i in range(n)]
        crosses = [crossProduct(vectors[(i-1)%n],vectors[i]) for i in range(n)]
        # print(vectors)
        # print(crosses)
        pre = 0
        for i in range(n):
            if crosses[i] != 0:
                if pre * crosses[i] < 0:
                    return False
                pre = crosses[i]
        return True

