from collections import Counter, deque

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M = 10**9 + 7
        dp = [deque() for _ in range(6)]
        sums = Counter()
        for i in range(6):
            for j in range(rollMax[i]):
                dp[i].append(0)
            dp[i].popleft()
            dp[i].append(1)
            sums[i] = 1
        for i in range(1,n):
            maxs = Counter()
            for j in range(6):
                maxs[j] = dp[j].popleft()
                zeros = 0
                for k in range(6):
                    if k != j:
                        zeros += sums[k]
                        zeros %= M 
                dp[j].append(zeros)
            for j in range(6):
                sums[j] = sums[j] - maxs[j] + dp[j][-1]
                sums[j] %= M 
        res = 0
        for j in range(6):
            res += sums[j]
            res %= M 
        return res


# from collections import Counter

# class Solution:
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         M = 10**9 + 7
#         dp = [[0]*rollMax[i] for i in range(6)]
#         sums = Counter()
#         for i in range(6):
#             dp[i][-1] = 1
#             sums[i] = 1
#         for i in range(1,n):
#             maxs = Counter()
#             for j in range(6):
#                 maxs[j] = dp[j][0]
#                 dp[j] = dp[j][1:]
#                 zeros = 0
#                 for k in range(6):
#                     if k != j:
#                         zeros += sums[k]
#                         zeros %= M 
#                 dp[j].append(zeros)
#             for j in range(6):
#                 sums[j] = sums[j] - maxs[j] + dp[j][-1]
#                 sums[j] %= M 
#         res = 0
#         for j in range(6):
#             res += sums[j]
#             res %= M 
#         return res
