# class Solution:
#     def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
#         res = []
#         qset =set()
#         for q in queens:
#             qset.add((q[0],q[1]))
#         row, col = king[0], king[1]
#         for up in range(row-1,-1,-1):
#             if (up,col) in qset:
#                 res.append([up,col])
#                 break
#         for down in range(row+1,8):
#             if (down,col) in qset:
#                 res.append([down,col])
#                 break
#         for left in range(col-1,-1,-1):
#             if (row,left) in qset:
#                 res.append([row,left])
#                 break
#         for right in range(col+1,8):
#             if (row,right) in qset:
#                 res.append([row,right])
#                 break
#         for k in range(1,8):
#             r, c = row+k, col+k
#             if r >= 8 or c >= 8:
#                 break
#             if (r,c) in qset:
#                 res.append([r,c])
#                 break
#         for k in range(1,8):
#             r, c = row-k, col+k
#             if r < 0 or c >= 8:
#                 break
#             if (r,c) in qset:
#                 res.append([r,c])
#                 break
#         for k in range(1,8):
#             r, c = row-k, col-k
#             if r < 0 or c < 0:
#                 break
#             if (r,c) in qset:
#                 res.append([r,c])
#                 break
#         for k in range(1,8):
#             r, c = row+k, col-k
#             if r >= 8 or c < 0:
#                 break
#             if (r,c) in qset:
#                 res.append([r,c])
#                 break
#         return res

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for k in range(8):
                    r = x*k + king[0]
                    c = y*k + king[1]
                    if r < 0 or c < 0 or r >= 8 or c >= 8:
                        break
                    if [r,c] in queens:
                        res.append([r,c])
                        break
        return res