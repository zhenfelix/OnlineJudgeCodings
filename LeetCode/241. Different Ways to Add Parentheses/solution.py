          
# from itertools import product
# from collections import defaultdict
# class Solution:
#     def diffWaysToCompute(self, input: str) -> List[int]:
#         input += " "
#         nums, ops = [], []
#         cur = ''
#         for i, ch in enumerate(input):
#             if ch < '0' or ch > '9':
#                 nums.append(int(cur))
#                 cur = ''
#                 ops.append(ch)
#             else:
#                 cur += ch
#         n = len(nums)
#         memo = defaultdict(list)
#         def dfs(i,j):
#             if (i,j) in memo:
#                 return memo[i,j]
#             if i == j:
#                 memo[i,j] = [nums[i]]
#                 return memo[i,j]
#             for k in range(i,j):
#                 left, right = dfs(i,k), dfs(k+1,j)
#                 # if ops[k] == '-':
#                 #     memo[i,j] += [l-r for l in left for r in right]
#                 # elif ops[k] == '+':
#                 #     memo[i,j] += [l+r for l in left for r in right]
#                 # else:
#                 #     memo[i,j] += [l*r for l in left for r in right]
#                 # memo[i,j] += [eval("l"+ops[k]+"r") for l in left for r in right]
#                 memo[i,j] += [eval(str(p[0])+ops[k]+str(p[1])) for p in product(left,right)]
#             return memo[i,j]
                
#         return dfs(0,n-1)
#         

from functools import lru_cache

class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]