# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = {}
#         def dfs(t):
#             if t in dp:
#                 return dp[t]
#             if t == 0:
#                 return 1
#             if t < 0:
#                 return 0
#             ans = 0
#             for n in nums:
#                 ans += dfs(t-n)
#             dp[t]=ans
#             return ans 
#         return dfs(target)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combos = [0] * (target + 1)
        #nums.sort()
        for i in range(target + 1):
            for n in nums:
                if n < i:
                    combos[i] += combos[i-n]
                elif n == i:
                    combos[i] += 1
                    
        return(combos[target])