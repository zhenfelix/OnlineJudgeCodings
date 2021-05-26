# class Solution:
#     def stoneGameVIII(self, stones: List[int]) -> int:
#         n = len(stones)
#         presums = [0]
#         for stone in stones:
#             presums.append(presums[-1]+stone)
#         if n == 2:
#             return presums[-1]
#         dp = [0]*n
#         f = [-float('inf')]*n
#         f[-1] = presums[n]-dp[n-1]
#         for i in range(n-1)[::-1]:
#             dp[i] = f[i+1]
#             f[i] = max(f[i+1], presums[i+1]-dp[i])
#         # print(presums)
#         # print(dp)
#         # print(f)
#         return f[0]
#WA Solution
# [32,-10,-12]


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        presums = [0]
        for stone in stones:
            presums.append(presums[-1]+stone)
        # if n == 2:
        #     return presums[-1]
        dp = [0]*n
        f = [-float('inf')]*n
        f[-1] = presums[n]-dp[n-1]
        for i in range(n-1)[::-1]:
            dp[i] = f[i+1]
            f[i] = max(f[i+1], presums[i+1]-dp[i])
        # print(presums)
        # print(dp)
        # print(f)
        return dp[0]