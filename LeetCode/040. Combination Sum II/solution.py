from functools import lru_cache
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        pre = [-1]*n 
        for i in range(n):
            if candidates[i] == candidates[i-1]:
                pre[i] = pre[i-1]
            else:
                pre[i] = i-1

        @lru_cache(None)
        def dfs(i, sums):
            if sums == 0:
                return [[]]
            if i < 0 or sums < 0:
                return []
            res = dfs(pre[i], sums)
            res2 = dfs(i-1, sums-candidates[i])
            # print(i,sums,res,res2)
            # for c in res2:
            #     res.append(c+[candidates[i]])
            # print(i,sums,res)
            return res+[c+[candidates[i]] for c in res2]
        return dfs(len(candidates)-1, target)

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         print(candidates)
#         dp = collections.defaultdict(set)
#         dp[0] = set([()])
#         for candidate in candidates:
#             # if candidate > target:
#             #     break
#             for x in range(candidate,target+1)[::-1]:
#                 if x-candidate in dp:
#                     for nums in dp[x-candidate]:
#                         dp[x].add(nums+(candidate,))
#             # print(dp)
#         return list(map(list,dp[target]))
    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # print(candidates)
        dp = collections.defaultdict(list)
        dp[0] = [[]]
        for idx in range(len(candidates)):
            for x in range(candidates[idx],target+1)[::-1]:
                if x-candidates[idx] in dp:
                    for nums in dp[x-candidates[idx]]:
                        if idx > 0 and candidates[idx] == candidates[idx-1] and (not nums or nums[-1] != idx-1):
                            continue
                        dp[x].append(nums+[idx])
            # print(dp)
        # print(dp[target])
        return [list(map(lambda idx: candidates[idx], nums)) for nums in dp[target]]
    
# class Solution:
#     def combinationSum2(self, candidates, target):
#         # Sorting is really helpful, se we can avoid over counting easily
#         candidates.sort()                      
#         result = []
#         self.combine_sum_2(candidates, 0, [], result, target)
#         return result
        
#     def combine_sum_2(self, nums, start, path, result, target):
#         # Base case: if the sum of the path satisfies the target, we will consider 
#         # it as a solution, and stop there
#         if not target:
#             result.append(path)
#             return
        
#         for i in range(start, len(nums)):
#             # Very important here! We don't use `i > 0` because we always want 
#             # to count the first element in this recursive step even if it is the same 
#             # as one before. To avoid overcounting, we just ignore the duplicates
#             # after the first element.
#             if i > start and nums[i] == nums[i - 1]:
#                 continue

#             # If the current element is bigger than the assigned target, there is 
#             # no need to keep searching, since all the numbers are positive
#             if nums[i] > target:
#                 break

#             # We change the start to `i + 1` because one element only could
#             # be used once
#             self.combine_sum_2(nums, i + 1, path + [nums[i]], 
#                                result, target - nums[i])