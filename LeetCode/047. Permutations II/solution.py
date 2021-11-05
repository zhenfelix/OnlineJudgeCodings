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
                #notice arr[i] is the previous valid value at position i
                #remaining elements are still sorted!
                arr[i], arr[k] = arr[k], arr[i]
                dfs(i+1, arr.copy())  
                # arr[i], arr[k] = arr[k], arr[i] # very important to use copy instead of swap
            return   
        nums.sort()
        dfs(0,nums.copy())
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, arr):
            if i == n:
                res.append(arr.copy())
                return
            for k in range(i,n):
                if k != i and arr[i] == arr[k]: continue 
                #notice arr[i] is the previous valid value at position i
                #remaining elements are still sorted!
                arr[i], arr[k] = arr[k], arr[i]
                dfs(i+1, arr)  
                # arr[i], arr[k] = arr[k], arr[i] # very important to use copy instead of swap
            cur = arr[i]
            for j in range(i,n-1):
                arr[j] = arr[j+1]
            arr[-1] = cur
            return   
        nums.sort()
        dfs(0,nums)
        return res



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i,arr):
            if i == n:
                res.append(arr.copy())
                return
            used = set()
            for k in range(i,n):
                if nums[k] in used:
                    continue
                used.add(nums[k])
                arr[i], arr[k] = arr[k], arr[i]
                dfs(i+1,arr)
                arr[i], arr[k] = arr[k], arr[i]
            return
        dfs(0,nums)
        return res
