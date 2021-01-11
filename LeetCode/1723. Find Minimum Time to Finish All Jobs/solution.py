# from functools import lru_cache
# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
#         n = len(jobs)
#         tmp = {0: 0}
#         for i in range(n):
#             tmp[1<<i] = jobs[i]
#         cost = [0]*(1<<n)
#         for i in range(1<<n):
#             cost[i] = cost[i&(i-1)] + tmp[i-(i&(i-1))]
#         # print(cost,tmp)
#         @lru_cache(None)
#         def dfs(idx, state):
#             res = float('inf')
#             if idx == k:
#                 return res if state else 0
#             if state == 0:
#                 return 0
#             cur = state
#             total = cost[state]
#             while cur:
#                 t = cost[cur]
#                 # print(idx,cur,t)
#                 if t < res:
#                     res = min(res, max(t,dfs(idx+1,state-cur)))
#                 cur = (cur-1)&state
#             # print(idx,state,res,'memo')
#             return res 
#         return dfs(0,(1<<n)-1)

# from functools import lru_cache
# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
#         n = len(jobs)
#         tmp = {0: 0}
#         for i in range(n):
#             tmp[1<<i] = jobs[i]
#         cost = [0]*(1<<n)
#         for i in range(1<<n):
#             cost[i] = cost[i&(i-1)] + tmp[i-(i&(i-1))]
#         # print(cost,tmp)
#         @lru_cache(None)
#         def dfs(idx, state):
#             res = float('inf')
#             if idx == k:
#                 return res if state else 0
#             if state == 0:
#                 return 0
#             cur = state
#             total = cost[state]
#             while cur:
#                 t = cost[cur]
#                 # print(idx,cur,t)
#                 if t < res:
#                     res = min(res, max(t,dfs(idx+1,state-cur)))
#                 cur = (cur-1)&state
#             # print(idx,state,res,'memo')
#             return res 
#         return dfs(0,(1<<n)-1)


from functools import lru_cache
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        tmp = {0: 0}
        for i in range(n):
            tmp[1<<i] = jobs[i]
        cost = [0]*(1<<n)
        for i in range(1<<n):
            cost[i] = cost[i&(i-1)] + tmp[i-(i&(i-1))]
        # print(cost,tmp)
        @lru_cache(None)
        def dfs(idx, state):
            res = float('inf')
            if idx == k:
                return res if state else 0
            if state == 0:
                return 0
            state_ = state&(state-1)
            cur = state_
            fixed = state - state_ 
            while True:
                t = cost[cur|fixed]
                # print(idx,cur,t)
                if t < res:
                    res = min(res, max(t,dfs(idx+1,state_-cur)))
                if cur == 0:
                    break
                cur = (cur-1)&state_
            # print(idx,state,res,'memo')
            return res 
        return dfs(0,(1<<n)-1)

