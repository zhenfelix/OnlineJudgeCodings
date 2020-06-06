# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         res = []
#         def dfs(path):
#             if len(path) == n:
#                 res.append(path)
#                 return
#             for i, num in enumerate(nums):
#                 if num in path:
#                     continue
#                 dfs(path+[num])
#             return
#         dfs([])
#         return res
                
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i,arr):
            if i == n:
                res.append(arr)
                return
            for k in range(i,n):
                arr[i], arr[k] = arr[k], arr[i]
                dfs(i+1,arr.copy())
            return
        dfs(0,nums.copy())
        return res
                