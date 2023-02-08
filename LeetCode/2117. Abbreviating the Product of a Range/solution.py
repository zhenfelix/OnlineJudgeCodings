class Solution:

    def abbreviateProduct(self, left: int, right: int) -> str:

        C, maxpre, mod, maxval = 0, 10 ** 24, 10 ** 10, 10 ** 12

        val, pre, suf = 1,1,1

        for i in range(left, right + 1):

            pre *= i

            suf *= i

            last = 0

            while pre > maxpre :

                last = pre % 10

                pre = pre // 10

            if last >= 5:

                pre += 1

            while suf % 10 == 0:

                suf //= 10

                C += 1

            suf %= mod

            if val <= maxval:

                val *= i

                while val % 10 == 0:

                    val //= 10

        

        if len(str(val)) <= 10:

            return str(val) + 'e' + str(C)

        else:

            p, s = str(pre), str(suf)

            while len(p) > 5:

                p = p[:-1]

            while len(s) > 5:

                s = s[1:]

            while len(s) < 5:

                s = '0' + s

            return p + '...' + s + 'e' + str(C)

作者：newhar
链接：https://leetcode.cn/problems/abbreviating-the-product-of-a-range/solutions/1176934/fen-bie-ji-suan-qian-5wei-he-hou-5wei-si-dc9x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




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

