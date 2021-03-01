# class Solution:
#     def translateNum(self, num: int) -> int:
#         s = str(num)
#         n = len(s)
#         dp = [0]*(n+2)
#         dp[-1] = 1
#         for i in range(n):
#             dp[i] = dp[i-1] 
#             if i-1 >= 0 and '0' < s[i-1] < '3' and '10' <= s[i-1:i+1] <= '25':
#                 dp[i] += dp[i-2]
#         return dp[n-1]

# class Solution:
#     def translateNum(self, num: int) -> int:
#         s = str(num)
#         a, b = 1, 1
#         for i in range(len(s) - 2, -1, -1):
#             a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
#         return a

class Solution:
    def translateNum(self, num: int) -> int:
        r = 0
        a, b = 1, 0
        while num:
            r += (num%10)*100
            r //= 10
            num //= 10
            a, b = (a + b if 10 <= r <= 25 else a), a
        return a