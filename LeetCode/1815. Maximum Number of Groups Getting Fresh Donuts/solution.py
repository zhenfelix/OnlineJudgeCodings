# class Solution:
#     def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
#         groups = [n % batchSize for n in groups]
#         cnt = [0] * batchSize
#         for n in groups:
#             cnt[n] += 1
#         ans = {}
#         def f(remain, cnt):
#             tcnt = tuple(cnt)
#             if (remain, tcnt) in ans:
#                 return ans[(remain, tcnt)]
#             if sum(cnt) == 0:
#                 ans[(remain, tcnt)] = 0
#                 return 0
#             curans = 0
#             for n in range(batchSize):
#                 if cnt[n] > 0:
#                     cnt[n] -= 1
#                     curans = max(curans, f((remain - n) % batchSize, cnt))
#                     cnt[n] += 1
#             curans += 0 if remain else 1
#             ans[(remain, tcnt)] = curans
#             return curans
#         return f(0, cnt)


# from functools import lru_cache
# class Solution:
#     def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
#         groups = [n % batchSize for n in groups]
#         cnt = [0] * batchSize
#         for n in groups:
#             cnt[n] += 1
#         ans = {}
#         @lru_cache(None)
#         def f(remain, tcnt):
            
#             if sum(tcnt) == 0:
#                 return 0
#             curans = 0
#             for n in range(batchSize):
#                 if cnt[n] > 0:
#                     cnt[n] -= 1
#                     curans = max(curans, f((remain - n) % batchSize, tuple(cnt)))
#                     cnt[n] += 1
#             curans += 0 if remain else 1
#             return curans
#         return f(0, tuple(cnt))

from functools import lru_cache
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        groups = [n % batchSize for n in groups]
        cnt = [0] * batchSize
        for n in groups:
            cnt[n] += 1
        ans = cnt[0]
        for n in range(1,batchSize):
            t = min(cnt[n],cnt[batchSize-n]) if n*2 != batchSize else cnt[n]//2
            cnt[n] -= t
            cnt[batchSize-n] -= t 
            ans += t 
        cnt[0] = 0
        # print(ans,cnt)
            
        @lru_cache(None)
        def f(remain, tcnt):
            
            if sum(tcnt) == 0:
                return 0
            curans = 0
            for n in range(1,batchSize):
                if cnt[n] > 0:
                    cnt[n] -= 1
                    curans = max(curans, f((remain - n) % batchSize, tuple(cnt)))
                    cnt[n] += 1
            curans += 0 if remain else 1
            return curans
        return f(0, tuple(cnt)) + ans