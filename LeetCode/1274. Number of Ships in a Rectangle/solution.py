# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#   def __init__(self, x: int, y: int):
#       self.x = x
#       self.y = y

# class Solution(object):
#     def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
#         if not sea.hasShips(topRight,bottomLeft):
#             return 0
#         x1, y1 = bottomLeft.x, bottomLeft.y
#         x2, y2 = topRight.x, topRight.y 
#         if x1 == x2 and y1 == y2:
#             return 1
#         cnt = 0
#         if x1 == x2:
#             cnt += self.countShips(sea, Point(x2,y2), Point(x2,(y1+y2)//2+1))
#             cnt += self.countShips(sea, Point(x1,(y1+y2)//2), Point(x1,y1))
#         elif y1 == y2:
#             cnt += self.countShips(sea, Point(x2,y2), Point((x1+x2)//2+1,y2))
#             cnt += self.countShips(sea, Point((x1+x2)//2,y1), Point(x1,y1))
#         else:
#             cnt += self.countShips(sea, Point(x2,y2), Point((x1+x2)//2+1,(y1+y2)//2+1))
#             cnt += self.countShips(sea, Point((x1+x2)//2,y2), Point(x1,(y1+y2)//2+1))
#             cnt += self.countShips(sea, Point(x2,(y1+y2)//2), Point((x1+x2)//2+1,y1))
#             cnt += self.countShips(sea, Point((x1+x2)//2,(y1+y2)//2), Point(x1,y1))
#         return cnt 

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y 
        if x1 > x2 or y1 > y2 or not sea.hasShips(topRight,bottomLeft):
            return 0
        if x1 == x2 and y1 == y2:
            return 1
        cnt = 0
        x12, y12 = (x1+x2)//2, (y1+y2)//2
        cnt += self.countShips(sea, Point(x2,y2), Point(x12+1,y12+1))
        cnt += self.countShips(sea, Point(x12,y2), Point(x1,y12+1))
        cnt += self.countShips(sea, Point(x2,y12), Point(x12+1,y1))
        cnt += self.countShips(sea, Point(x12,y12), Point(x1,y1))
        return cnt 


# hack

    # def countShips(self, sea, P, Q):
    #     return sum(Q.x <= x <= P.x and Q.y <= y <= P.y for x, y in sea._Sea__ans)

    # print(dir(sea))



class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        hix, hiy = topRight.x, topRight.y 
        lox, loy = bottomLeft.x, bottomLeft.y 
        if hix == lox and hiy == loy:
            return sea.hasShips(topRight,bottomLeft)
        if not sea.hasShips(topRight,bottomLeft):
            return 0
        if hix == lox:
            mid = (hiy+loy)//2
            return self.countShips(sea, Point(lox,mid), bottomLeft) + self.countShips(sea, topRight, Point(lox,mid+1))
        mid = (hix+lox)//2
        return self.countShips(sea, topRight, Point(mid+1,loy)) + self.countShips(sea, Point(mid,hiy), bottomLeft)