# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         # print(s)
#         cc = 0
#         res = ""
#         rev = ""
#         for i, ch in enumerate(s):
#             if ch == '(':
#                 cc += 1
#                 if cc == 1:
#                     continue
#             elif ch == ')':
#                 cc -= 1
#                 if cc == 0:
#                     res += self.reverseParentheses(rev)[::-1]
#                     rev = ""
#                     continue
            
#             if cc >= 1:
#                 rev += ch
#             else:
#                 res += ch
       
#         return res
#                 

class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        for ch in s:
            if ch != ')':
                res.append(ch)
            else:
                tmp = ""
                while True:
                    back = res.pop()
                    if back == '(': break
                    tmp += back
                res += tmp
        return "".join(res)
                    