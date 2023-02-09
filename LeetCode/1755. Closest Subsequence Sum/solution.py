# class Solution:
#     def minAbsDifference(self, nums: List[int], goal: int) -> int:
#         nums.sort()
#         # print(nums)
#         n, res = len(nums), float('inf')
#         cur = {0:-1}
#         for level in range(n+1):
#             nxt = {}
#             tmp = []
#             for k in cur:
#                 res = min(res,abs(goal-k))
                
#                 # if cur[k]-level == 5:
#                 #     tmp.append((level,k,cur[k]))
#                     # print(level,k,cur[k])
#                 for i in range(cur[k]+1,n):
#                     # if k+nums[i] == 10804:
#                     #     print(level,k,cur[k],nums[i])
#                     if k+nums[i] not in nxt:
#                         nxt[k+nums[i]] = i 
#                     else:
#                         nxt[k+nums[i]] = min(nxt[k+nums[i]],i)
#             cur = nxt
#             # if tmp:
#             #     print(tmp[-1])
#         # print(cur)
#         return res 

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        m = n//2
        n -= m
        right, left = nums[:m], nums[-n:]
        def generate(arr):
            res = [0]
            for a in arr:
                sz = len(res)
                for i in range(sz):
                    res.append(res[i]+a)
            return sorted(res)
        left = generate(left)
        right = generate(right)
        n, m = len(left), len(right)
        j = m-1
        ans = inf
        for i in range(n):
            a = left[i]
            
            while j >= 0 and a+right[j] > goal:
                ans = min(ans, abs(a+right[j]-goal))
                j -= 1
            if j >= 0:
                ans = min(ans, abs(a+right[j]-goal))
            else:
                ans = min(ans, abs(a-goal))
        return ans 


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n, res = len(nums), float('inf')
        def gen(left,right):
            arr = set([0])
            for i in range(left,right+1):
                tmp = set()
                for v in arr:
                    tmp.add(v+nums[i])
                arr |= tmp
            # print(arr)
            return list(arr)

        arr1, arr2 = gen(0,n//2-1), sorted(gen(n//2,n-1))
        # print(arr1,arr2)
        for cur in arr1:
            idx = bisect.bisect_right(arr2, goal-cur)-1
            if idx >= 0:
                res = min(res, abs(goal-cur-arr2[idx]))
            if idx+1 < len(arr2):
                res = min(res, abs(goal-cur-arr2[idx+1]))
        return res


# class Solution:
#     def minAbsDifference(self, nums: List[int], goal: int) -> int:
#         ranges=[[0,0] for _ in range(len(nums)+1)]
#         for i in range(len(nums)-1,-1,-1):
#             mi,ma=ranges[i+1]
#             ranges[i]=[min(mi,mi+nums[i]),max(ma,ma+nums[i])]
            
#         @lru_cache(None)
#         def dfs(idx,s):
#             if idx==len(nums):
#                 return 0
#             mi,ma=ranges[idx]
#             if s<=mi:
#                 ans=mi
#             elif s>=ma:
#                 ans=ma
#             else:
#                 tmp1=dfs(idx+1,s)
#                 if tmp1==s:
#                     ans=tmp1
#                 else:
#                     v=nums[idx]
#                     tmp2=dfs(idx+1,s-v)
#                     if abs(tmp1-s)<abs(tmp2+v-s):
#                         ans=tmp1
#                     else:
#                         ans=tmp2+v
#             return ans
#         return abs(goal-dfs(0,goal))
        