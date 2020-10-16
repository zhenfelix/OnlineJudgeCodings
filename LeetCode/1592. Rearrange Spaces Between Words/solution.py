class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split() # split(sep=None) will discard empty strings.
        # print(words)
        cnt = len(words)
        spaces = text.count(' ')
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
        trailing_spaces = spaces if gap == 0 else spaces % (cnt - 1)
        return (' ' * gap).join(words) + ' ' * trailing_spaces        

# class Solution:
#     def reorderSpaces(self, text: str) -> str:
#         arr = [x for x in text.split(' ') if x]
#         # print(arr)
#         n = len(arr)
#         cnt = len(text) - len(''.join(arr))
#         m, r = 0, cnt
#         if n > 1:
#             m, r = cnt//(n-1), cnt%(n-1)
#         res = []
#         for i, a in enumerate(arr):
#             res.append(a)
#             if i != n-1:
#                 res[-1] += ' '*m
#             else:
#                 res[-1] += ' '*r 
#         return ''.join(res)