# class Solution:
#     def alphabetBoardPath(self, target: str) -> str:
#         def move(dx, isRow = True):
#             if isRow:
#                 if dx >= 0:
#                     return "D"*dx
#                 else:
#                     return "U"*(-dx)
#             else:
#                 if dx >= 0:
#                     return "R"*dx
#                 else:
#                     return "L"*(-dx)
            
            
#         board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
#         mp = {}
#         for i, row in enumerate(board):
#             for j, ch in enumerate(row):
#                 mp[ch] = [i,j]
        
#         ans = ""
#         pre = [0,0]
#         for t in target:
#             cur = mp[t]
#             drow, dcol = cur[0]-pre[0], cur[1]-pre[1]
#             if cur[0] == 5:
#                 ans += move(dcol,False)
#                 ans += move(drow)
#             else:
#                 ans += move(drow)
#                 ans += move(dcol,False)
#             ans += "!"
#             pre = cur
#         return ans

class Solution:
    def alphabetBoardPath(self, target):
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)        