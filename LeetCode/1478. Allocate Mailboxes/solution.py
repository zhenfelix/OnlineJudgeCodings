
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])

        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n: return 0
            if k == 0 or i == n: return math.inf
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]  # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)


class Solution:
    def minDistance(self, A, k):
        A.sort()
        n = len(A)
        B = [0]
        for i, a in enumerate(A):
            B.append(B[i] + a)

        def cal(i, j):
            m1, m2 = (i + j) // 2, (i + j + 1) // 2
            return (B[j + 1] - B[m2]) - (B[m1 + 1] - B[i])

        dp = [cal(0, j) for j in range(n)]
        for k in range(2, k + 1):
            for j in range(n - 1, k - 2, -1):
                for i in range(k - 2, j):
                    dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
        return dp[-1]


# from functools import lru_cache
# class Solution:

#     def minDistance(self, houses: List[int], K: int) -> int:
#         @lru_cache(None)
#         def dfs(n,k):
#             if n == k:
#                 return 0
#             if k == 1:
#                 res = 0
#                 i, j = 0, n-1
#                 while i < j:
#                     res += houses[j]-houses[i]
#                     i += 1
#                     j -= 1
#                 return res
#             res = float('inf')
#             tmp = 0
#             for m in range(k-1,n)[::-1]:
#                 if m < n-1:
#                     tmp += houses[m+1]-houses[m]
#                 if m < n-3:
#                     tmp += houses[m+2]-houses[m+1]
#                 if m < n-5:
#                     tmp += houses[m+3]-houses[m+2]
#                 res = min(res,tmp+dfs(m,k-1))
#             # print(n,k,tmp,res)
#             return res
        
#         houses.sort()
#         # print(houses)
#         return dfs(len(houses),K)