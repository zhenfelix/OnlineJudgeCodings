class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        d = collections.Counter(nums)
        quantity.sort(reverse=True)
        def dfs(i):
            if i >= len(quantity):
                return True
            for k in d.keys():
                if d[k] >= quantity[i]:
                    d[k] -= quantity[i]
                    if dfs(i+1):
                        return True
                    d[k] += quantity[i]
            return False
        return dfs(0)


# class Solution:
#     def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
#         cc = list(Counter(nums).values())
#         n, m = len(cc), len(quantity)
#         def dfs(idx, state):
#             if state == (1<<m) - 1:
#                 return True
#             if idx == n:
#                 return False
#             for nxt in range(1<<m):
#                 if state&nxt == state:
#                     tmp = (~state)&nxt
#                     if sum(quantity[i] for i in range(m) if (1<<i)&tmp) <= cc[idx] and dfs(idx+1,nxt):
#                         return True
#             return False
#         return dfs(0,0)

# from functools import lru_cache
# class Solution:
#     def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
#         cc = list(Counter(nums).values())
#         n, m = len(cc), len(quantity)
#         sums = [0]*(1<<m)
#         for s in range(1<<m):
#             delta = s&(-s)
#             if delta:
#                 sums[s] = sums[s-delta] + quantity[len(bin(delta))-3]
#         @lru_cache(None)
#         def dfs(idx, todo):
#             if todo == 0:
#                 return True
#             if idx == n:
#                 return False
#             s = todo
#             while 1:
#                 if sums[s] <= cc[idx] and dfs(idx+1,todo-s):
#                     return True
#                 if s == 0:
#                     break
#                 s = (s-1)&todo
#             return False
#         return dfs(0,(1<<m)-1)

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cc = list(Counter(nums).values())
        n, m = len(cc), len(quantity)
        sums = [0]*(1<<m)
        for s in range(1<<m):
            delta = s&(-s)
            if delta:
                sums[s] = sums[s-delta] + quantity[len(bin(delta))-3]
        dp = [[False]*(1<<m) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        def submask(mask):
            s = mask
            while s:
                yield s 
                s = (s-1)&mask
            return
        for i in range(n):
            for state in range(1<<m):
                if dp[i-1][state]:
                    dp[i][state] = True
                    continue
                for cur in submask(state):
                    if sums[cur] <= cc[i] and dp[i-1][state-cur]:
                        dp[i][state] = True
                        break
        return dp[n-1][-1]

# class Solution:
#     def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
#         cc = list(Counter(nums).values())
#         n, m = len(cc), len(quantity)
#         sums = [0]*(1<<m)
#         for s in range(1<<m):
#             delta = s&(-s)
#             if delta:
#                 sums[s] = sums[s-delta] + quantity[len(bin(delta))-3]
#         dp = [[False]*(1<<m) for _ in range(n+1)]
#         for i in range(n+1):
#             dp[i][0] = True
#         def submask(mask):
#             s = mask
#             while 1:
#                 yield s 
#                 if s == 0:
#                     break
#                 s = (s-1)&mask
#             return
#         for i in range(n):
#             for state in range(1<<m):
#                 # if dp[i-1][state]:
#                 #     dp[i][state] = True
#                 #     continue
#                 for cur in submask(state):
#                     if sums[cur] <= cc[i] and dp[i-1][state-cur]:
#                         dp[i][state] = True
#                         break
#         return dp[n-1][-1]
