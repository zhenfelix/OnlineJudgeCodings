from functools import lru_cache
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        rods = sorted(rods)[::-1]
        n = len(rods)
        psum = rods.copy()
        for i in range(n-1)[::-1]:
            psum[i] += psum[i+1]

        @lru_cache(None)
        def dfs(idx, diff):
            if idx == n:
                return 0 if diff == 0 else -float('inf')
            if diff > psum[idx]:
                return -float('inf')
            return max(dfs(idx+1,diff),dfs(idx+1,diff+rods[idx]),dfs(idx+1,abs(diff-rods[idx]))+min(diff,rods[idx]))
        return dfs(0,0)


# from functools import lru_cache
# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#         rods = sorted(rods)[::-1]
#         n = len(rods)
#         psum = rods.copy()
#         for i in range(n-1)[::-1]:
#             psum[i] += psum[i+1]

#         @lru_cache(None)
#         def dfs(idx, left, right):
#             if idx == n:
#                 return left if left == right else 0
#             if abs(left-right) > psum[idx]:
#                 return 0
#             return max(dfs(idx+1,left+rods[idx],right),dfs(idx+1,left,right+rods[idx]),dfs(idx+1,left,right))
#         return dfs(0,0,0)


# from functools import lru_cache
# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#         n = len(rods)
#         mp = defaultdict(list)
#         for i in range(1<<n):
#             sums = 0
#             for k in range(n):
#                 if i & (1<<k):
#                     sums += rods[k]
#             mp[sums].append(i)
#         for k in sorted(mp)[::-1]:
#             if 2*k in mp:
#                 v = mp[k]
#                 m = len(v)
#                 for i in range(m):
#                     for j in range(i+1,m):
#                         if v[i] & v[j] == 0:
#                             return k
#         return 0
