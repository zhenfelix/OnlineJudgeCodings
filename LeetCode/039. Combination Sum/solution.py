# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates = sorted(candidates)
#         memo = {}
#         def dfs(idx, t):
#             if (idx,t) in memo:
#                 return memo[idx,t]
#             if idx >= len(candidates) or t <= 0 or candidates[idx] > t:
#                 memo[idx,t] = []
#                 return []
#             if candidates[idx] == t:
#                 memo[idx,t] = [[candidates[idx]]]
#                 return memo[idx,t]
            
#             ans = []
#             if dfs(idx,t-candidates[idx]) != []:
#                 ans = dfs(idx,t-candidates[idx])
#                 ans = [[candidates[idx]]+p for p in ans]
#             if dfs(idx+1,t) != []:
#                 ans += dfs(idx+1,t)
#             memo[idx,t] = ans
#             return ans
#         return dfs(0,target)


# class Solution:
#     def combinationSum(self, candidates, target):
#         res = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, [], res)
#         return res
        
#     def dfs(self, nums, target, index, path, res):
#         if target < 0:
#             return  # backtracking
#         if target == 0:
#             res.append(path)
#             return 
#         for i in range(index, len(nums)):
#             self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = collections.defaultdict(list)
        dp[0] = [[]]
        for candidate in candidates:
            for x in range(candidate,target+1):
                if x-candidate in dp:
                    for nums in dp[x-candidate]:
                        dp[x].append(nums+[candidate])
        return dp[target]


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         dp = collections.defaultdict(list)
#         dp[0] = [[]]
#         for x in range(1,target+1):
#             for candidate in candidates:
#                 if x-candidate in dp:
#                     for nums in dp[x-candidate]:
#                         dp[x].append(nums+[candidate])
#             print(dp)
#         return dp[target]