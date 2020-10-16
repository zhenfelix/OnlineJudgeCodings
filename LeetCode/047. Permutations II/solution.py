# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         cnt = Counter(nums)
#         ns = set(nums)
#         def dfs(path):
#             if len(path) == n:
#                 res.append(path.copy())
#                 return
#             for i in ns:
#                 c = cnt[i]
#                 if c <= 0: continue
#                 if path and path[-1] == i: continue
#                 for j in range(1,c+1):
#                     cnt[i] -= 1
#                     path.append(i)
#                     dfs(path)
#                 for j in range(1,c+1):
#                     cnt[i] += 1
#                     path.pop()
#             return
#         dfs([])
#         return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, arr):
            if i == n:
                res.append(arr)
                return
            for k in range(i,n):
                if k != i and arr[i] == arr[k]: continue
                arr[i], arr[k] = arr[k], arr[i]
                dfs(i+1, arr.copy())  
                # arr[i], arr[k] = arr[k], arr[i] # very important to use copy instead of swap
            return   
        nums.sort()
        dfs(0,nums.copy())
        return res
