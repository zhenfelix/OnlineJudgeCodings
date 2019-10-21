class Solution:
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     n = len(coordinates)
    #     if n == 2:
    #         return True
    #     x0, y0 = coordinates[0][0], coordinates[0][1]
    #     x1, y1 = coordinates[1][0], coordinates[1][1]
    #     for i in range(2,n):
    #         x, y = coordinates[i][0], coordinates[i][1]
    #         if (y-y1)*(x-x0) != (y-y0)*(x-x1):
    #             return False
    #     return True
    
    def checkStraightLine(self, A):
        i,j = A[0], A[1]
        return all(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1] == 0 for k in A)