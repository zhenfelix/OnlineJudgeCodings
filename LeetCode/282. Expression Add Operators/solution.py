# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         n = len(num)
#         res =[]
#         if not num:
#             return res
#         def dfs(idx, cur):
#             if idx == n:
#                 # print(cur)
#                 try:
#                     if eval(cur) == target and eval(cur+"*1") == target:
#                         res.append(cur)
#                 except:
#                     pass
#                 return

#             for sym in ['+','-','*']:
#                 dfs(idx+1,cur+sym+num[idx])
#             dfs(idx+1,cur+num[idx])
#             return
#         dfs(1,num[0])
#         return res