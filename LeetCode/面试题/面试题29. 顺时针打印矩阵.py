# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix:
#             return []
#         n, m = len(matrix), len(matrix[0])
#         res, idx = [], 0
#         r, c = 0, 0
#         while idx < n*m:
#             while idx < n*m and c < m and matrix[r][c] != None:
#                 res.append(matrix[r][c])
#                 matrix[r][c] = None
#                 idx += 1
#                 c += 1
#             r += 1
#             c -= 1
#             while idx < n*m and r < n and matrix[r][c] != None:
#                 res.append(matrix[r][c])
#                 matrix[r][c] = None
#                 idx += 1
#                 r += 1
#             r -= 1
#             c -= 1
#             while idx < n*m and c >= 0 and matrix[r][c] != None:
#                 res.append(matrix[r][c])
#                 matrix[r][c] = None
#                 idx += 1
#                 c -= 1
#             r -= 1
#             c += 1
#             while idx < n*m and r >= 0 and matrix[r][c] != None:
#                 res.append(matrix[r][c])
#                 matrix[r][c] = None
#                 idx += 1
#                 r -= 1
#             r += 1
#             c += 1
#         return res

class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
