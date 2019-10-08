# class Solution:
#   def longestSubsequence(self, arr: List[int], difference: int) -> int:
#     dp = {}
#     ans = 0
#     for x in arr:
#       if x - difference not in dp:
#         dp[x] = 1
#       else:
#         dp[x] = dp[x-difference] + 1
#       ans = max(ans, dp[x])
      
#     return ans

class Solution:
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
    dp = {}
    ans = 0
    for x in arr:
      dp[x] = dp.get(x-difference,0) + 1
      ans = max(ans, dp[x])
      
    return ans