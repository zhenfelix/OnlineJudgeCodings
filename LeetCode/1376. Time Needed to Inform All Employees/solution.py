class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         memo = [-1]*n
#         memo[headID] = 0
#         res = 0
        
#         def dfs(cur):
#             if memo[cur] >= 0:
#                 return memo[cur]
#             parent = manager[cur]
#             memo[cur] = informTime[parent] + dfs(parent)
#             return memo[cur]
        
#         for i in range(n):
#             res = max(res,dfs(i))        
#         return res
                
    
    def numOfMinutes(self, n, headID, manager, informTime):
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, range(n)))