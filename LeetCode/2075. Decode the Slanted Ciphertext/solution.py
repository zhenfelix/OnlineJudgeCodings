# class Solution:
#     def decodeCiphertext(self, encodedText: str, rows: int) -> str:
#         n = len(encodedText)
#         cols = n//rows
#         mat = [[' ']*cols for _ in range(rows)]
#         for i, ch in enumerate(encodedText):
#             r = i//cols
#             c = i%cols
#             if ch != ' ':
#                 mat[r][c] = ch 
#         res = []
#         for j in range(cols):
#             i = 0
#             while j < cols and i < rows:
#                 res.append(mat[i][j])
#                 i += 1
#                 j += 1
#         while res and res[-1] == ' ':
#             res.pop()
#         return ''.join(res)


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n//rows
        res = []
        for j in range(cols):
            while j < n:
                res.append(encodedText[j])
                j += cols+1
        while res and res[-1] == ' ':
            res.pop()
        return ''.join(res)