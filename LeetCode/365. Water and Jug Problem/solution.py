# class Solution:
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         def gcd(a,b):
#             if b == 0:
#                 return a
#             return gcd(b, a%b)
#         if x < y:
#             x, y = y, x
#         return z <= x and z%gcd(x,y) == 0



# class Solution:
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         if z > x+y:
#             return False
#         q = collections.deque()
#         q.append((0,0))
#         visited = set([(0,0)])
#         while q:
#             a, b = q.popleft()
#             if a + b == z:
#                 return True
#             for i, j in set([(x,b),(a,y),(0,b),(a,0),(max(0,a+b-y),min(a+b,y)),(min(a+b,x),max(0,a+b-x))]):
#                 if (i,j) not in visited:
#                     visited.add((i,j))
#                     q.append((i,j))
#         return False

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x+y:
            return False
        q = collections.deque([0,x,y])
        visited = set([0,x,y])
        while q:
            cur = q.popleft()
            if cur == z:
                return True
            if cur < 0 or cur > x + y:
                continue
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    nxt = cur + i*x + j*y
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
        return False

