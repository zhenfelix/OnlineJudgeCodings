# from functools import lru_cache
# class Solution:
#     def connectTwoGroups(self, cost: List[List[int]]) -> int:
#         n, m = len(cost), len(cost[0])
#         @lru_cache(None)
#         def dfs(idx, state):
#             if idx == n:
#                 if state + 1 == 1<<m:
#                     return 0
#                 return float('inf')
#             res = float('inf')
#             for nxt in range(1,1<<m):
#                 res = min(res, dfs(idx+1, state|nxt) + sum(cost[idx][j] for j in range(m) if 1<<j&nxt))
#             return res
        
#         return dfs(0,0)


from functools import lru_cache
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])
        @lru_cache(None)
        def dfs(idx, state, left):
            if left:
                if idx == n:
                    return dfs(0, state, False)
                return min(dfs(idx+1, state|(1<<j), left) + cost[idx][j] for j in range(m))
            else:
                if idx == m:
                    return 0
                if state & (1<<idx):
                    return dfs(idx+1, state, left)
                return min(dfs(idx+1, state|(1<<idx), left) + cost[i][idx] for i in range(n))
        return dfs(0,0,True)


    # def connectTwoGroups(self, cost: List[List[int]]) -> int:
    #     sz1, sz2 = len(cost), len(cost[0])
    #     min_sz2 = [min([cost[i][j] for i in range(sz1)]) for j in range(sz2)]
    #     @lru_cache(None)
    #     def dfs(i: int, mask: int):
    #         res = 0 if i >= sz1 else float('inf')
    #         if i >= sz1:
    #             for j in range(sz2):
    #                 if mask & (1 << j) == 0:
    #                     res += min_sz2[j]
    #         else:
    #             for j in range(sz2):
    #                 res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))
    #         return res
    #     return dfs(0, 0)