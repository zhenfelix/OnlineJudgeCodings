class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        def gcd(a,b):
            if a < b: a, b = b, a
            while b:
                a, b = b, a%b
            return a

        res, candidate, n = 0, [], len(points)
        for i in range(n):
            lines = defaultdict(list)
            zeros, multiplicity = [], 1
            for j in range(i+1,n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x1,y1) == (x2,y2):
                    multiplicity += 1
                elif x1 == x2:
                    zeros.append(j)
                else:
                    x, y = x2-x1, y2-y1
                    flag = 1
                    if x < 0: x, y = -x, -y
                    if y < 0: flag, y = -flag, -y
                    k = gcd(x,y)
                    x, y = x//k, flag*y//k
                    lines[x,y].append(j)
            lines = [lines[x,y] for x,y in lines]
            tmp = max([zeros]+lines, key=lambda x: len(x))
            if len(tmp)+multiplicity > res:
                res = len(tmp)+multiplicity
                candidate = [i,tmp[0]]
        return candidate