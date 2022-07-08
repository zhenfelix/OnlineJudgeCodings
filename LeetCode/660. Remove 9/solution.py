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

        
# class Solution:
#     def newInteger(self, n: int) -> int:
#         fac = [1]
#         for i in range(10):
#             fac.append(fac[-1]*9)
#         def calc(x):
#             y = x 
#             base = 1
#             idx = 0
#             while base <= x:
#                 base *= 10
#                 idx += 1
#             base //= 10
#             idx -= 1
#             cnt = 0
#             while base:
#                 cur = x//base
#                 cnt += cur*(base-fac[idx])
#                 x %= base
#                 base //= 10
#                 idx -= 1
#                 if cur == 9:
#                     cnt += x+1
#                     break
#             return y-cnt

#         lo, hi = 1, 10**10
#         while lo <= hi:
#             mid = (lo+hi)//2
#             # print(mid,calc(mid))
#             if calc(mid) >= n:
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


# 作者：LeetCode
# 链接：https://leetcode.cn/problems/remove-9/solution/yi-chu-9-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

