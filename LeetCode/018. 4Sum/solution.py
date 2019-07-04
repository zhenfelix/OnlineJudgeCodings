# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         ans, tmp = [], []
#         nums = sorted(nums)
#         mp = {}
#         def dfs(t, idx, cc):
#             if cc == 4:
#                 if t == 0:
#                     if tuple(tmp.copy()) not in mp:
#                         ans.append(tmp.copy())
#                         mp[tuple(tmp.copy())] = True
#                 return
#             if idx == len(nums):
#                 return
            
#             dfs(t,idx+1,cc)
#             tmp.append(nums[idx])
#             dfs(t-nums[idx],idx+1,cc+1)
#             tmp.pop()
#         dfs(target,0,0)
#         return ans

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums = sorted(nums)
#         results = []
#         def dfs(idx, N, t, result):
#             if N == 0 and t == 0:
#                 # print(result)
#                 results.append(result)
#                 return
#             if idx < len(nums):
#                 for i in range(idx,len(nums)-N+1):
#                     if t < nums[i]*N or t > nums[-1]*N:
#                         break
#                     elif i == idx or nums[i] != nums[i-1]:
#                         dfs(i+1, N-1, t-nums[i], result+[nums[i]])
#             return
#         dfs(0,4,target,[])
#         return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        def dfs(idx, N, t, result):
            if N == 2:
                left, right = idx, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == t:
                        results.append(result+[nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                        
                    elif nums[left]+nums[right] > t:
                        right -= 1
                    else:
                        left += 1
                
                return
               
            for i in range(idx,len(nums)-N+1):
                if t < nums[i]*N or t > nums[-1]*N:
                    break
                if i == idx or nums[i] != nums[i-1]:
                    dfs(i+1, N-1, t-nums[i], result+[nums[i]])     
            return
        dfs(0,4,target,[])
        return results
                    
            