# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         n = len(satisfaction)
#         dp = [0]+[-float('inf')]*n
#         for i, s in enumerate(satisfaction):
#         	for j in range(1,i+2)[::-1]:
#         		dp[j] = dp[j-1]+j*satisfaction[i]
#         return max(dp)

class Solution:
    def maxSatisfaction(self, A):
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            res += total
        return res