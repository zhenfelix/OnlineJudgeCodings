# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         mod = 10**9 + 7
#         # ans 表示答案，shift 表示 len_{2}(i)
#         ans = shift = 0
#         for i in range(1, n + 1):
#             # if 131072 % i == 0:
#             if (i & (i - 1)) == 0:
#                 shift += 1
#             ans = ((ans << shift) + i) % mod
#         return ans


# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/solution/lian-jie-lian-xu-er-jin-zhi-shu-zi-by-ze-t40j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         res, base, pre = 0, 1, 0
#         MOD = 10**9+7
#         for i in range(1,n+1)[::-1]:
#             # print(i)
#             tmp = bin(i)
#             base *= (1<<pre)
#             pre = len(tmp)-2
#             base %= MOD
#             res += i*base
#             res %= MOD
#         return res 

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        # ans 表示答案，shift 表示 len_{2}(i)
        ans, base = 0, 1
        for i in range(1, n + 1):
            # if 131072 % i == 0:
            if (i & (i - 1)) == 0:
                base *= 2
                base %= mod 
            ans = (ans * base + i) % mod
        return ans