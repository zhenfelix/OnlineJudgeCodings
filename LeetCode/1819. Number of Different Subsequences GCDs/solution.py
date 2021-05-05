# class Solution:
#     def countDifferentSubsequenceGCDs(self, nums):
#         T = max(nums) + 1
#         nums = set(nums)
#         ans = 0
            
#         for x in range(1, T):
#             g = 0
#             for y in range(x, T, x):
#                 if y in nums:
#                     g = gcd(g, y)
#                 if g == x:
#                     break
                    
#             if g == x: ans += 1
                
#         return ans

class Solution:
    def countDifferentSubsequenceGCDs(self, nums):
        nums = set(nums)
        T = max(nums) + 1
        dp = [True if i in nums else False for i in range(T+1)]
        ans = 0
            
        for x in range(1, T+1)[::-1]:
            if not dp[x]:
                g = 0
                for y in range(x, T+1, x):
                    if dp[y]:
                        g = gcd(g, y)
                    if g == x:
                        dp[x] = True
                        break
                    
            if dp[x]: ans += 1
                
        return ans