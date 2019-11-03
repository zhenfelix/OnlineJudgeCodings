# from collections import defaultdict
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#         dp = [defaultdict(list) for _ in range(n)]
#         sums = 0
#         for i in range(n):
#             # print(i, dp[i])
#             for j in range(i):
#                 delta = A[i]-A[j]
#                 # print(i, delta)
#                 if delta not in dp[j]:
#                     dp[i][delta] += [0]
#                 else:
#                     dp[i][delta] += [sum(x+1 for x in dp[j][delta])]
#             # print(i, dp[i])
#             for k, v in dp[i].items():
#                 sums += sum(v)
#         return sums

    
class Solution:
    def numberOfArithmeticSlices(self, A):
        from collections import defaultdict
        total = 0
        dp = [defaultdict(int) for item in A]
        for i in range(len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] += 1
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                    total += dp[j][A[i]-A[j]]
        return total