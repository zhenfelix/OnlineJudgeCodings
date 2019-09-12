# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         res = ""
#         for center in range(n*2-1):
#             left, right = (center-1)//2, center//2+1
#             while left >= 0 and right < n and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             if len(res) < right-left-1:
#                 res = s[left+1:right]
#         return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ss = ['#']*(2*n-1)
        dp = [i for i in range(2*n-1)]
        center, reach = 0, 0
        # res_center, res_reach = 0, 0
        for i in range(n):
            ss[i*2] = s[i]
            
        for i in range(2*n-1):
            if i < reach and dp[2*center-i]-(2*center-i)+i < reach:
                dp[i] = dp[2*center-i]-(2*center-i)+i
                continue
            right = reach+1
            left = 2*i-right
            while left >= 0 and right < 2*n-1 and ss[left] == ss[right]:
                left -= 1
                right += 1
            center, reach = i, right-1
            dp[i] = reach
         
        r, l = 0, 0
        for i, reach in enumerate(dp):
            right, left = reach, 2*i-reach
            if left & 1 == 1:
                left += 1
            right //= 2
            left //= 2
            if right-left > r-l:
                r, l = right, left
        # print(dp)
        # print(res_center,res_reach)
        return s[l:r+1]