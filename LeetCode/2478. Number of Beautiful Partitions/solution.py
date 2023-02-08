class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9+7
        primes = "2357"
        arr = [0 if ch in primes else 1 for ch in s]
        n = len(arr)
        if arr[0] != 0 or arr[-1] != 1:
            return 0
        for i in range(n-1):
            if arr[i+1] == 1:
                arr[i] = 0
        dp = [1]*(n+1)
        for _ in range(k):
            ndp = [0]*(n+1)
            for i in range(minLength-1,n):
                ndp[i+1] = ndp[i]
                if arr[i] == 1:
                    ndp[i+1] = (ndp[i+1]+dp[i+1-minLength])%MOD
            dp = ndp
        return (dp[-1]-dp[-2])%MOD

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9+7
        primes = "2357"
        arr = []
        for ch in s:
            if ch in primes:
                arr.append(0)
            else:
                arr.append(1)
        n = len(arr)
        if arr[0] != 0 or arr[-1] != 1:
            return 0
        for i in range(n-1):
            if arr[i+1] == 1:
                arr[i] = 0
        # print(arr)
        @lru_cache(None)
        def dfs(i, r):
            if i < 0:
                return 0
            if i == 0:
                return 1 if r == 0 else 0
            if r < 0:
                return 0
            res = dfs(i-1,r)
            if arr[i-1] == 1:
                res = (res+dfs(i-minLength,r-1))%MOD
            # print(i,r,res)
            return res 
        # print(dfs(n,k))
        return (dfs(n,k)-dfs(n-1,k))%MOD


# class Solution:
#     def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
#         primes = "2357"
#         arr = []
#         for ch in s:
#             if ch in primes:
#                 arr.append(0)
#             else:
#                 arr.append(1)
#         n = len(arr)
#         if arr[0] != 0 or arr[-1] != 1:
#             return 0
#         cnt = 1
#         nums = []
#         for i in range(1,n):
#             if arr[i] == 0 and arr[i-1] == 1:
#                 nums.append(cnt)
#                 cnt = 0
#             cnt += 1
#         if cnt > 0:
#             nums.append(cnt)
#         m = len(nums)
#         if m < k:
#             return 0
#         # print(nums)
#         sums = [0]
#         for a in nums:
#             sums.append(sums[-1]+a)
#         pre = [0]*m
#         j = 0
#         for i in range(m):
#             while sums[i+1]-sums[j] >= minLength:
#                 j += 1
#             pre[i] = j-1
#         MOD = 10**9+7
#         @lru_cache(None)
#         def dfs(i, r, flag):
#             if i < 0:
#                 return 0 
#             if i == 0:
#                 if flag:
#                     return 0 
#                 else:
#                     if r == 0:
#                         return 1
#                     return 0
#             if r < 0:
#                 return 0
#             if flag:
#                 return (dfs(i-1,r-1,False)+dfs(i-1,r,True))%MOD
#             else:
#                 j = pre[i-1]
#                 return (dfs(j,r-1,False)+dfs(j,r,True))%MOD
            
#             return 0
#         return dfs(m,k,False)%MOD

