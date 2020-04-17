# class Solution:
#     def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
#         if x1 <= x_center <= x2 and y1 <= y_center <= y2:
#             return True
#         if x1 <= x_center <= x2:
#             if abs(y1-y_center) <= radius or abs(y2-y_center) <= radius:
#                 return True
#             else:
#                 return False
#         elif y1 <= y_center <= y2:
#             if abs(x1-x_center) <= radius or abs(x2-x_center) <= radius:
#                 return True
#             else:
#                 return False
#         else:
#             for x, y in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
#                 if (x-x_center)**2+(y-y_center)**2 <= radius**2:
#                     return True
#             return False

class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        # Translate everything so circle is centered at (0, 0)
        x1 -= x_center
        y1 -= y_center
        x2 -= x_center
        y2 -= y_center
        
        # Let's choose point in square closest to the origin
        x = x1 if x1 > 0 else x2 if x2 < 0 else 0
        y = y1 if y1 > 0 else y2 if y2 < 0 else 0
        return x ** 2 + y ** 2 <= radius ** 2