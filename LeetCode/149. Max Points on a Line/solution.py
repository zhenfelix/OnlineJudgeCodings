class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a,b):
            a, b = max(a,b), min(a,b)
            while b != 0:
                a, b = b, a%b
            return a

        res = 0
        points = [tuple(point) for point in points]
        n = len(points)
        for i in range(n):
            cc = collections.Counter()
            mutiplicity, zeros, tmp = 1, 0, 0
            for j in range(i+1,n):
                if points[j] == points[i]:
                    mutiplicity += 1
                elif points[j][0] == points[i][0]:
                    zeros += 1
                    tmp = max(tmp,zeros)
                else:
                    x, y = points[j][0]-points[i][0], points[j][1]-points[i][1]
                    if x < 0:
                        x, y = -x, -y
                    d = gcd(abs(y),x)
                    x, y = x//d, y//d
                    cc[x,y] += 1
                    tmp = max(tmp,cc[x,y])
            res = max(res,mutiplicity+tmp)
        return res

