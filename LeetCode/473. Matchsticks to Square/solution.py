# from functools import lru_cache
# class Solution:
#     def makesquare(self, nums: List[int]) -> bool:
#         total, n = sum(nums), len(nums)
#         target = total//4
#         if target*4 != total or not nums:
#             return False
            
#         @lru_cache(None)
#         def dfs(idx,a,b,c):
#             # print(idx,a,b,c)
#             if any(x > target for x in [a,b,c]) or min(a,b,c) > total-sum([a,b,c]):
#                 return False
#             if idx == n:
#                 return sum(x for x in [a,b,c]) + target == total
#             return any([dfs(idx+1,a,b,c), dfs(idx+1,a+nums[idx],b,c), dfs(idx+1,a,b+nums[idx],c), dfs(idx+1,a,b,c+nums[idx])])
#         return dfs(0,0,0,0)


# class Solution:
#     def makesquare(self, nums: List[int]) -> bool:
#         n = len(nums)
#         total = sum(nums)
#         if not nums or total%4:
#             return False
#         dp = [0]*(1<<n)
#         mp = defaultdict(set)
#         for i in range(1,1<<n):
#             # dp[i] = sum(nums[j] for j in range(n) if i&(1<<j))
#             delta = i&(-i)
#             dp[i] = dp[i-delta] + nums[len(bin(delta))-3]
#             mp[dp[i]].add(i)
#         for p in mp[total//2]:
#             q = (1<<n)-1-p
#             if q not in mp[total//2]: continue
#             f1, f2 = False, False
#             for x in mp[total//4]:
#                 y = p - x
#                 z = q - x
#                 if p == x|y and y in mp[total//4]:
#                     f1 = True
#                 if q == x|z and z in mp[total//4]:
#                     f2 = True
#                 if f1 and f2:
#                     return True
#         return False

# class Solution:
#     def makesquare(self, nums: List[int]) -> bool:
#         nums.sort(reverse=True)
#         n = len(nums)
#         total = sum(nums)
#         if not nums or total%4:
#             return False
#         target = total//4
#         def dfs(idx, edges):
#             if any(sz > target for sz in edges):
#                 return False
#             if idx == n:
#                 return True
#             for i in range(4):
#                 if edges[i] + nums[idx] <= target:
#                     edges[i] += nums[idx]
#                     if dfs(idx+1,edges):
#                         return True
#                     edges[i] -= nums[idx]
#             return False
#         return dfs(0,[0,0,0,0])

# class Solution(object):
#     def makesquare(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         def dfs(nums, pos, target):
#             if pos == len(nums): return True
#             for i in range(4):
#                 if target[i] >= nums[pos]:
#                     target[i] -= nums[pos]
#                     if dfs(nums, pos+1, target): return True
#                     target[i] += nums[pos]
#             return False
#         if len(nums) < 4 : return False
#         numSum = sum(nums)
#         nums.sort(reverse=True)
#         if numSum % 4 != 0: return False
#         target = [numSum/4] * 4;
#         return dfs(nums,0, target)


class Solution:
    def makesquare(self, A: List[int]) -> bool:
        if len(A) < 4 or sum(A) % 4 or max(A) > sum(A) // 4:
            return False

        T = sum(A) // 4
        N = len(A)
        A.sort()

        memo = {}
        def dp(mask, cur = T):
            if (mask, cur) in memo: return memo[mask, cur]
            if mask == 0: return cur == 0
            if cur == 0: return dp(mask, T)
            ans = False
            for bit in range(N):
                if mask & (1 << bit):
                    if A[bit] > cur:
                        break
                    if dp(mask ^ (1 << bit), cur - A[bit]):
                        ans = True
                        break
            memo[mask, cur] = ans
            return ans

        return dp(2**N - 1)