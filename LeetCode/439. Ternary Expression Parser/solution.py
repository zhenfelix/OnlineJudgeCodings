# class Solution:
#     def parseTernary(self, expression: str) -> str:
#       ops = []
#       expr = [[]]
#       token = ''
#       expression = expression + ':'
#       idx = {'T':0, 'F':1}
#       for ch in expression:
#         if ch == '?':
#           ops.append(token)
#           expr.append([])
#         elif ch == ':':
#           expr[-1].append(token)
#           while len(expr[-1]) == 2:
#             op = ops.pop()
#             token = expr.pop()[idx[op]]
#             expr[-1].append(token)
#         else:
#           token = ch
#       return expr[0][0]

# class Solution:
#     def parseTernary(self, expression: str) -> str:

#         stk = list(expression)
#         k = list()
#         while stk:
#             c = stk.pop()
#             if c == '?':
#                 if stk.pop() == 'F':
#                     k.pop()
#                 else:
#                     a = k.pop()
#                     k.pop()
#                     k.append(a)
#             elif c != ":":
#                 k.append(c)
#         return k[0]

class Solution:
    def parseTernary(self, expression: str) -> str:

        def dfs(i):
          if i+1 >= len(expression) or expression[i+1] != '?':
            return expression[i], i+2
          op = expression[i]
          i += 2
          first, i = dfs(i)
          second, i = dfs(i)
          return first if op == 'T' else second, i 
        return dfs(0)[0]