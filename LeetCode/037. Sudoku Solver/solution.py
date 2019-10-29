# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         candidates = []
#         for i, row in enumerate(board):
#             for j, num in enumerate(row):
#                 if board[i][j] == '.':
#                     candidates.append((i,j))

#         n = len(candidates)
#         def dfs(idx):
#             if idx == n:
#                 return True
#             r, c = candidates[idx]
#             for cur in range(1,10):
#                 cur = str(cur)
#                 if findInLine(cur,r,c) or findInBox(cur,r,c):
#                     continue
#                 board[r][c] = cur
#                 if dfs(idx+1):
#                     return True
#                 board[r][c] = '.'
#             return False

#         def findInLine(cur,x,y):
#             xx = x
#             for yy in range(9):
#                 if (xx,yy) == (x,y):
#                     continue
#                 if board[xx][yy] == cur:
#                     return True
#             yy = y
#             for xx in range(9):
#                 if (xx,yy) == (x,y):
#                     continue
#                 if board[xx][yy] == cur:
#                     return True
#             return False

#         def findInBox(cur,x,y):
#             box_x, box_y = x//3, y//3
#             for i in range(3):
#                 for j in range(3):
#                     xx, yy = 3*box_x+i, 3*box_y+j
#                     if (xx,yy) == (x,y):
#                         continue
#                     if board[xx][yy] == cur:
#                         return True
#             return False
#         dfs(0)
#         return

from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        candidates = []
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if board[i][j] == '.':
                    candidates.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[i//3,j//3].add(board[i][j])

        n = len(candidates)
        def dfs(idx):
            if idx == n:
                return True
            r, c = candidates[idx]
            for cur in range(1,10):
                cur = str(cur)
                if cur in rows[r] or cur in cols[c] or cur in boxes[r//3,c//3]:
                    continue
                board[r][c] = cur
                rows[r].add(cur)
                cols[c].add(cur)
                boxes[r//3,c//3].add(cur)
                if dfs(idx+1):
                    return True
                rows[r].remove(cur)
                cols[c].remove(cur)
                boxes[r//3,c//3].remove(cur)
                board[r][c] = '.'
            return False

        dfs(0)
        return
