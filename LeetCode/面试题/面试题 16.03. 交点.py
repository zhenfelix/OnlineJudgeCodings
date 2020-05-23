class Solution:
    def cross(self, x1,y1,x2,y2):
        return x1*y2-x2*y1


    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        a1, b1 = end1[1] - start1[1], end1[0] - start1[0]
        c1 = self.cross(start1[0],start1[1],end1[0],end1[1])
        a2, b2 = end2[1] - start2[1], end2[0] - start2[0]
        c2 = self.cross(start2[0],start2[1],end2[0],end2[1])
        ab = -self.cross(a1,b1,a2,b2)
        if start1 > end1:
            start1, end1 = end1, start1
        if start2 > end2:
            start2, end2 = end2, start2
        
        if ab == 0:            
            if start2 > end1 or start1 > end2:
                return []
            res = max(start1, start2)
            return res if self.cross(end1[0]-res[0],end1[1]-res[1],end2[0]-res[0],end2[1]-res[1]) == 0 else []
        else:
            bc = self.cross(b1,c1,b2,c2)
            ac = self.cross(a1,c1,a2,c2)
            x = bc/ab
            y = ac/ab
            res = [x,y]
            return res if start1 <= res <= end1 and start2 <= res <= end2 else []
