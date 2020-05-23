# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         p1, p2, p3, p4 = sorted([p1,p2,p3,p4])
#         if p1[0]-p2[0] != p3[0]-p4[0] or p1[1]-p2[1] != p3[1]-p4[1]:
#             return False
#         if p1[0]-p3[0] != p2[0]-p4[0] or p1[1]-p3[1] != p2[1]-p4[1]:
#             return False
#         if (p1[0]-p3[0])*(p1[0]-p2[0]) + (p1[1]-p3[1])*(p1[1]-p2[1]) != 0:
#             return False
#         if (p1[0]-p4[0])*(p3[0]-p2[0]) + (p1[1]-p4[1])*(p3[1]-p2[1]) != 0:
#             return False
#         if p1[0] == p2[0] and p1[1] == p2[1]:
#             return False
#         return True


# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         p1, p2, p3, p4 = sorted([p1,p2,p3,p4])
#         if p1 == p2: return False
#         if p1[0]+p4[0] == p2[0]+p3[0] and p1[1]+p4[1] == p2[1]+p3[1] and (p1[0]-p4[0])*(p2[0]-p3[0])+(p1[1]-p4[1])*(p2[1]-p3[1]) == 0 and (p1[0]-p4[0])**2+(p1[1]-p4[1])**2 == (p2[0]-p3[0])**2+(p2[1]-p3[1])**2:
#             return True
#         return False

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]
        
        dists = collections.Counter()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dists[self.getDistance(points[i], points[j])] += 1
        
        return len(dists.values())==2 and 4 in dists.values() and 2 in dists.values()
        
    def getDistance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2