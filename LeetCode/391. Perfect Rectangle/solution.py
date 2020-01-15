# class Solution:
#     def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
#         n = len(rectangles)
#         for i in range(n):
#             for j in range(i+1,n):
#                 left1, down1, right1, up1 = rectangles[i]
#                 left2, down2, right2, up2 = rectangles[j]
#                 if left1 < right2 and left2 < right1 and down1 < up2 and down2 < up1:
#                     return False

#         sums = 0
        
#         left, down, right, up = float("inf"), float("inf"), -float("inf"), -float("inf")
#         for l,d,r,u in rectangles:
#             left = min(left,l)
#             down = min(down,d)
#             right = max(right,r)
#             up = max(up,u)
#             sums += (r-l)*(u-d)
#         # print(sums)
#         return sums == (right-left)*(up-down)


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        sums = 0
        
        left, down, right, up = float("inf"), float("inf"), -float("inf"), -float("inf")
        for l,d,r,u in rectangles:
            left = min(left,l)
            down = min(down,d)
            right = max(right,r)
            up = max(up,u)
            sums += (r-l)*(u-d)
            corners ^= set({(l,d),(r,u),(l,u),(r,d)})
        # print(sums)
        return corners == set({(left,down),(right,up),(left,up),(right,down)}) and sums == (right-left)*(up-down)
    
# [[0,0,1,1],[0,2,1,3],[1,1,2,2],[2,0,3,1],[2,2,3,3],[1,0,2,3],[0,1,3,2]]
