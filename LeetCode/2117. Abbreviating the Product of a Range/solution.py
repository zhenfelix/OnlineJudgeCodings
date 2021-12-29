from functools import reduce
from math import log10

MOD = 100000

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        if right - left + 1 <= 50:
            ans = reduce(lambda x, y: x * y, range(left, right + 1), 1)
            s = str(ans)
            t = s.rstrip('0')
            z = len(s) - len(t)
            if len(t) <= 10:
                return t + 'e' + str(z)
            else:
                return t[:5] + '...' + t[-5:] + 'e' + str(z)
        else:
            l = sum(map(log10, range(left, right + 1)))
            L = str(10 ** (l - trunc(l)) * 10000)[:5]
            
            R = 1
            two = 0
            five = 0
            for i in range(left, right + 1):
                num = i
                while num % 2 == 0:
                    two += 1
                    num >>= 1
                while num % 5 == 0:
                    five += 1
                    num //= 5
                R = R * num % MOD
                
            z = min(two, five)
            R = R * pow(2, two - z, MOD) % MOD
            R = R * pow(5, five - z, MOD) % MOD
            return L + '...' + str(R).rjust(5, '0') + 'e' + str(z)


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/TNI0Rm/view/lriU08/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

