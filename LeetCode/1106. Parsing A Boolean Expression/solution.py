# class Solution:
#     def parseAnd(self, exp):
#         print('and',exp)
#         level, start = 0, 0
#         ans = True
#         for i, ch in enumerate(exp):
#             if ch == ',' and level == 0:
#                 ans = ans and self.parseBoolExpr(exp[start:i]) 
#                 start = i+1
#             elif ch == '(':
#                 level += 1
#             elif ch == ')':
#                 level -= 1
#             else:
#                 pass
#         ans = ans and self.parseBoolExpr(exp[start:])
#         return ans
    
#     def parseOr(self, exp):
#         print('or',exp)
#         level, start = 0, 0
#         ans = False
#         for i, ch in enumerate(exp):
#             if ch == ',' and level == 0:
#                 ans = ans or self.parseBoolExpr(exp[start:i]) 
#                 start = i+1
#             elif ch == '(':
#                 level += 1
#             elif ch == ')':
#                 level -= 1
#             else:
#                 pass
#         ans = ans or self.parseBoolExpr(exp[start:])
#         return ans
    
#     def parseNeg(self, exp):
#         print('neg',exp)
#         tmp =  self.parseBoolExpr(exp)
#         return not tmp
            
            
            
            
#     def parseBoolExpr(self, expression: str) -> bool:
#         print('expression',expression)
#         n = len(expression)
#         if expression[0] == '&':
#             return self.parseAnd(expression[2:n-1])
#         elif expression[0] == '|':
#             return self.parseOr(expression[2:n-1])
#         elif expression[0] == '!':
#             return self.parseNeg(expression[2:n-1])
#         elif expression[0] == 't':
#             return True
#         else:
#             return False
            
#                 




# class Solution:

#     def f(self, s):
#         # print(self.idx, s[self.idx:])
        
#         if s[self.idx] == 't':
#             self.idx += 1
#             ret = True
#         elif s[self.idx] == 'f':
#             self.idx += 1
#             ret = False
#         elif s[self.idx] == '!':
#             ret = self.f_not(s)
#         elif s[self.idx] == '&':
#             ret = self.f_and(s)
#         else:
#             ret = self.f_or(s)
#         # print(ret)
#         return ret


#     def f_not(self, s):
#         self.idx += 2
#         ret = self.f(s)
#         self.idx += 1
#         return not ret

#     def f_and(self, s):
#         self.idx += 2
#         ret = True 
#         ret = self.f(s) and ret #注意短路情况，所以要先调用函数再逻辑算符
#         while s[self.idx] != ')':
#             self.idx += 1
#             ret = self.f(s) and ret
#         self.idx += 1
#         return ret 

#     def f_or(self, s):
#         self.idx += 2
#         ret = False 
#         ret = self.f(s) or ret
#         while s[self.idx] != ')':
#             self.idx += 1
#             ret = self.f(s) or ret
#         self.idx += 1
#         return ret 

#     def parseBoolExpr(self, expression: str) -> bool:
#         self.idx = 0
#         return self.f(expression)


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        states, ops = [], []
        symbol = {'t':True, 'f':False}
        op2state = {'&':True, '|':False, '!':None}
        for ch in expression:
            if ch in '|&!':
                ops.append(ch)
            elif ch == '(':
                states.append(op2state[ops[-1]])
            elif ch in 'tf':
                op = ops[-1]
                if op == '!':
                    states[-1] = not symbol[ch]
                elif op == '&':
                    states[-1] = states[-1] and symbol[ch]
                elif op == '|':
                    states[-1] = states[-1] or symbol[ch]
            elif ch == ')':
                ops.pop()
                state = states.pop()
                if not ops:
                    return state
                op = ops[-1]
                if op == '!':
                    states[-1] = not state 
                elif op == '&':
                    states[-1] = states[-1] and state 
                elif op == '|':
                    states[-1] = states[-1] or state 
        return None


