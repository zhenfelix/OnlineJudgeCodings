# import functools
# class Solution:
#     def largestNumber(self, cost: List[int], target: int) -> str:
#         @functools.lru_cache(None)
#         def dfs(remains):
#             if remains < 0:
#                 return '0'
#             if remains == 0:
#                 return ''
#             res = '0'
#             for i in range(9):
#                 cur = dfs(remains-cost[i])
#                 if cur == '0':
#                     continue
#                 cur = str(i+1)+cur
#                 if len(cur) > len(res) or (len(cur) == len(res) and cur > res):
#                     res = cur
#             return res
#         return dfs(target)


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dfs(sums):
            if sums < 0:
                return "0"
            if sums == 0:
                return ""
            res = "0"
            for i, c in enumerate(cost):
                s = dfs(sums-c)+chr(ord("0")+i+1)
                # print(s,res,sums)
                if s[0] != "0" and (len(s) > len(res) or (len(s) == len(res) and s > res)):
                    res = s
            return res
        return dfs(target)

class Solution:
    def largestNumber(self, cost, target):
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))    


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dfs(idx, t):
            if t < 0:
                return "0"
            if idx == 0:
                return "" if t == 0 else "0"
            cur = dfs(idx-1, t)
            nxt = dfs(idx, t-cost[idx-1])
            if nxt != "0":
                nxt = str(idx)+nxt
                if len(nxt) > len(cur) or (len(nxt) == len(cur) and nxt > cur):
                    cur = nxt
            return cur
        return dfs(9, target)