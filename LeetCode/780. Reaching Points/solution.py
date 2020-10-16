# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         q = deque()
#         visited = set()
#         q.append((sx,sy))
#         visited.add((sx,sy))
#         while q:
#             curx, cury = q.popleft()
#             if (curx,cury) == (tx,ty):
#                 return True
#             if curx > tx or cury > ty:
#                 continue
#             if (curx+cury,cury) not in visited:
#                 q.append((curx+cury,cury))
#                 visited.add((curx+cury,cury))
#             if (curx,curx+cury) not in visited:
#                 q.append((curx,curx+cury))
#                 visited.add((curx,curx+cury))
#         return False

# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         if (sx,sy) == (tx,ty):
#             return True
#         if sx == tx:
#             return ty > tx and (ty-sy)%tx == 0 and (ty-sy)//tx > 0
#         if sy == ty:
#             return tx > ty and (tx-sx)%ty == 0 and (tx-sx)//ty > 0
#         if tx == ty or tx < sx or ty < sy:
#             return False
#         return self.reachingPoints(sx,sy,tx%ty,ty) if tx > ty else self.reachingPoints(sx,sy,tx,ty%tx)

class Solution:
    # def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    #     if tx > ty:
    #         sx, sy = sy, sx 
    #         tx, ty = ty, tx
    #     if sx == tx:
    #         return ty > tx and (ty-sy)%tx == 0 and (ty-sy)//tx >= 0
    #     if tx == ty or tx < sx or ty < sy:
    #         return False
    #     return self.reachingPoints(sx,sy,tx,ty%tx)
    
    def reachingPoints(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0