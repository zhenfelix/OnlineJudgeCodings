# from functools import lru_cache
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         @lru_cache(None)
#         def dfs(i,color,t):
#             if t <= 0:
#                 return float('inf')
#             tmp = 0
#             if i < m:
#                 if houses[i] > 0 and houses[i] != color:
#                         return float('inf')
#                 if houses[i] == 0:
#                     tmp = cost[i][color-1]
#             if i == 0:
#                 return tmp if t == 1 else float('inf')
#             res = float('inf')
#             for nxt in range(1,n+1):
#                 if nxt == color:
#                     res = min(res,dfs(i-1,nxt,t)+tmp)
#                 else:
#                     res = min(res,dfs(i-1,nxt,t-1)+tmp)
#             return res

#         ans = dfs(m,0,target+1)
#         return -1 if ans == float('inf') else ans

                


from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i,color,t):
            if t <= 0 or t > i+1:
                return float('inf')
            tmp = 0
            if i < m:
                if houses[i] > 0 and houses[i] != color:
                        return float('inf')
                if houses[i] == 0:
                    tmp = cost[i][color-1]
            if i == 0:
                return tmp
            # res = float('inf')
            # for nxt in range(1,n+1):
            #     if nxt == color:
            #         res = min(res,dfs(i-1,nxt,t)+tmp)
            #     else:
            #         res = min(res,dfs(i-1,nxt,t-1)+tmp)
            return min(dfs(i-1,nxt,t-(nxt != color))+tmp for nxt in range(1,n+1))

        ans = dfs(m,0,target+1)
        return -1 if ans == float('inf') else ans

                


from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i,color,t):
            if i < 0 and t == 0:
                return 0
            if i < 0 or t == 0 or t > i+1:
            # if i < 0 or t == 0:
                return float('inf')
            tmp = 0
            if i < m:
                if houses[i] > 0 and houses[i] != color:
                        return float('inf')
                if houses[i] == 0:
                    tmp = cost[i][color-1]
 
            return min(dfs(i-1,nxt,t-(nxt != color))+tmp for nxt in range(1,n+1))

        ans = dfs(m,0,target+1)
        return -1 if ans == float('inf') else ans