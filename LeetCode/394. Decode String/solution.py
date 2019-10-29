# class Solution(object):
#     def decodeString(self, s):
#         stack = []
#         stack.append(["", 1])
#         num = ""
#         for ch in s:
#             if ch.isdigit():
#               num += ch
#             elif ch == '[':
#                 stack.append(["", int(num)])
#                 num = ""
#             elif ch == ']':
#                 st, k = stack.pop()
#                 stack[-1][0] += st*k
#             else:
#                 stack[-1][0] += ch
#         return stack[0][0]

class Solution:
    def decodeString(self, s: str) -> str:
        res, cnt = [''], ['']
        for ch in s:
            if '0' <= ch <= '9':
                cnt[-1] += ch
            elif ch == '[':
                cnt[-1] = int(cnt[-1])
                cnt.append('')
                res.append('')
            elif ch == ']':
                cnt.pop()
                res[-1] = res[-1]*cnt[-1]
                pre = res.pop()
                res[-1] += pre
                cnt[-1] = ''
            else:
                res[-1] += ch
        return res[-1]