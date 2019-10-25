# from collections import Counter

# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         cc = self.dfs(formula)
#         cc = cc.items()
#         cc = sorted(cc)
#         cc = [''.join([x[0],str(x[1])]) if x[1] > 1 else x[0] for x in cc]
#         return ''.join(cc)

#     def dfs(self,formula):
#         cc = Counter()
#         k, v = '', ''
#         def isKind(char):
#             if '0' <= char <= '9':
#                 return 1
#             elif 'A' <= char <= 'Z':
#                 return 2
#             elif 'a' <= char <= 'z':
#                 return 3
#             return 0

#         i = 0
#         while i < len(formula):
#             ch = formula[i]
#             kind = isKind(ch)
#             if kind == 1:
#                 v += ch
#                 i += 1
#             elif kind == 3:
#                 k += ch
#                 i += 1
#             else:
#                 if not v:
#                     v = '1'
#                 if k:
#                     cc[k] += int(v)
#                 k, v = '', ''
#                 if kind == 2:
#                     k = ch
#                     i += 1
#                 else:
#                     cnt = 1
#                     j = i + 1
#                     while j < len(formula) and cnt > 0:
#                         if formula[j] == '(':
#                             cnt += 1
#                         elif formula[j] == ')':
#                             cnt -= 1
#                         j += 1
#                     new_cc = self.dfs(formula[i+1:j-1])
#                     repeat = ''
#                     while j < len(formula) and isKind(formula[j]) == 1:
#                         repeat += formula[j]
#                         j += 1
#                     if not repeat:
#                         repeat = '1'
#                     repeat = int(repeat)
                        
#                     for name, value in new_cc.items():
#                         cc[name] += value*repeat
#                     i = j 
#         if k:
#             if not v:
#                 v = '1'
#             cc[k] += int(v)
#         return cc


# class Solution:
#     def countOfAtoms(self, formula):
#         dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0  
#         for c in formula[::-1]:
#             if c.isdigit():
#                 cnt += int(c) * (10 ** i)
#                 i += 1
#             elif c == ")":
#                 stack.append(cnt or 1)
#                 coeff *= cnt
#                 i = cnt = 0
#             elif c == "(":
#                 coeff //= stack.pop()
#                 i = cnt = 0
#             elif c.isupper():
#                 elem += c
#                 dic[elem[::-1]] += (cnt or 1) * coeff
#                 elem = ""
#                 i = cnt = 0
#             elif c.islower():
#                 elem += c
#         return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))

class Solution:
    def countOfAtoms(self, formula):
        element, cnt, multiplicity = '', '', [1]
        cc = collections.Counter()
        for ch in formula[::-1]:
            if '0' <= ch <= '9':
                cnt = ch + cnt
            elif ch == ')':
                cnt = int(cnt or '1')
                multiplicity.append(multiplicity[-1]*cnt)
                cnt = ''
            elif ch == '(':
                multiplicity.pop()
            elif 'A' <= ch <= 'Z':
                element = ch + element
                cnt = int(cnt or '1') * multiplicity[-1]
                cc[element] += cnt
                element, cnt = '', ''
            else:
                element = ch + element
        return "".join(k + ("" if v == 1 else str(v)) for k, v in sorted(cc.items()))



