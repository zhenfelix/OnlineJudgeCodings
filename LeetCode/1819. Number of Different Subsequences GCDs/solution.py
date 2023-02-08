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



# class Solution:
#     def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
#         mx = max(nums)
#         dp = [0]*(mx+1)
#         for a in nums:
#             dp[a] = 1
#         ans = 0
#         def factoring(x):
#             y = x 
#             f = 2
#             fs = []
#             while f*f <= y:
#                 if x%f == 0:
#                     while x%f == 0:
#                         x //= f 
#                     fs.append(f)
#                 f += 1 
#             if x > 1:
#                 fs.append(x)
#             return fs 

#         for i in range(1,mx+1)[::-1]:
#             if dp[i] == 0:   
#                 cnt = 0
#                 seen = set()
#                 for j in range(i*2,mx+1,i):
#                     if dp[j] == 0: continue
#                     fs = factoring(j//i)
#                     if all(f not in seen for f in fs):
#                         cnt += 1
#                     if cnt >= 2:
#                         dp[i] = 1
#                         break 
#                     for f in fs:
#                         seen.add(f)
#         # print(dp)
#         return sum(f for f in dp) 