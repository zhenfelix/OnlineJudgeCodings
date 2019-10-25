# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:
#         if not costs:
#             return 0
#         n, k = len(costs), len(costs[0])
#         dp = costs[0].copy()
#         for i in range(1,n):
#             first = [float('inf'), set()]
#             second = [float('inf'), set()]
#             for j in range(k):
#                 if dp[j] < first[0]:
#                     second = first.copy()
#                     first[0] = dp[j]
#                     first[1] = set([j])
#                 elif dp[j] == first[0]:
#                     first[1].add(j)
#                 elif dp[j] < second[0]:
#                     second[0] = dp[j]
#                     second[1] = set([j])
#                 elif dp[j] == second[0]:
#                     second[1].add(j)
#             # print(dp)
#             # print(first,second)
#             for j in range(k):
#                 if j in first[1] and len(first[1]) == 1:
#                     dp[j] = second[0] + costs[i][j]
#                 else:
#                     dp[j] = first[0] + costs[i][j]
#         return min(dp)


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        dp = costs[0].copy()
        for i in range(1,n):
            first = second = float('inf')
            idx = -1
            for j in range(k):
                if dp[j] < first:
                    second = first
                    first, idx = dp[j], j
                elif dp[j] == first:
                    idx = -1
                elif dp[j] < second:
                    second = dp[j]
            
            for j in range(k):
                if j == idx:
                    dp[j] = second + costs[i][j]
                else:
                    dp[j] = first + costs[i][j]
        return min(dp)