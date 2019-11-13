# class Solution:
#     def newInteger(self, n: int) -> int:
#         def cnt9(x, base):
#             if base == 1:
#                 return 1 if x == 9 else 0
#             a, b = x//base, x%base
#             if a == 9:
#                 return b + a*cnt9(base-1, base//10) + 1
#             else:
#                 return cnt9(b, base//10) + a*cnt9(base-1, base//10)


#         lo, hi = 1, 10**10
#         while lo <= hi:
#             mid = (lo+hi)//2
#             base_ = 1
#             while mid//base_ > 9:
#                 base_ *= 10
#             cnt = cnt9(mid, base_)
#             # print(mid, cnt)
#             if mid-cnt >= n:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return lo

        
class Solution(object):
    def newInteger(self, n):
        ans = ''
        while n:
            ans = str(n%9) + ans
            n //= 9
        return int(ans)

