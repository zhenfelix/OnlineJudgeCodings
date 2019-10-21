# import functools

# class Solution:
#     def smallestFactorization(self, a: int) -> int:
#         @functools.lru_cache(None)
#         def dfs(target):
#             if target < 10:
#                 return target, 1
#             res, digit = 1<<31, 0
#             for i in range(2,10):
#                 if target%i == 0:
#                     nxt, nxt_digit = dfs(target//i)
#                     if not nxt_digit:
#                         continue
#                     if nxt+i*10**(nxt_digit) < res:
#                         res = nxt+i*10**(nxt_digit)
#                         digit = nxt_digit+1
#             if res == 1<<31 :
#                 return 0, None
#             return res, digit
#         ans, _ = dfs(a)
#         return ans

class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 10:
            return a
        MAX = 1<<31
        ans = 0
        base = 1
        for i in range(9,1,-1):
            while a%i == 0:
                ans += i*base
                if ans > MAX:
                    return 0
                a //= i
                base *= 10
        if a != 1:
            return 0

        return ans