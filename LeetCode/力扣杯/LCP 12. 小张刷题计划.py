# from functools import lru_cache
# class Solution:
#     def minTime(self, time: List[int], M: int) -> int:
#         presum = time.copy()
#         premax = time.copy()
#         sum_, max_ = 0, 0
#         for i, t in enumerate(time):
#             sum_ += t
#             max_ = max(max_, t)
#             presum[i] = sum_
#             premax[i] = max_
#         # print(presum)
#         # print(premax)
#         @lru_cache(None)
#         def dfs(n,m):
#             if m >= n:
#                 return 0
#             if m == 1:
#                 return presum[n-1]-premax[n-1]
#             sums, curmax = 0, 0
#             res = float('inf')
#             for i in range(n)[::-1]:
#                 sums += time[i]
#                 curmax = max(curmax, time[i])
#                 if presum[i]/(m-1) < sums-curmax:
#                     break
#                 res = min(res, max(sums-curmax,dfs(i,m-1)))
#             return res
#         return dfs(len(time),M)


from functools import lru_cache
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        lo, hi = 0, 10**9
        while lo <= hi:
            mid = (lo+hi)//2
            presum, premax, k = 0, 0, 1
            for t in time:
                presum += t
                premax = max(premax,t)
                if presum-premax > mid:
                    k += 1
                    presum = t
                    premax = t
                if k > m:
                    break
            if k > m:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
