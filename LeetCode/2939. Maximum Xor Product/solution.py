class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a < b:
            a, b = b, a  # 保证 a >= b

        mask = (1 << n) - 1
        ax = a & ~mask  # 第 n 位及其左边，无法被 x 影响，先算出来
        bx = b & ~mask
        a &= mask  # 低于第 n 位，能被 x 影响
        b &= mask

        left = a ^ b  # 可分配：a XOR x 和 b XOR x 一个是 1 另一个是 0
        one = mask ^ left  # 无需分配：a XOR x 和 b XOR x 均为 1
        ax |= one  # 先加到异或结果中
        bx |= one

        # 现在要把 left 分配到 ax 和 bx 中
        # 根据基本不等式（均值定理），分配后应当使 ax 和 bx 尽量接近，乘积才能尽量大
        if left > 0 and ax == bx:
            # 尽量均匀分配，例如把 1111 分成 1000 和 0111
            high_bit = 1 << (left.bit_length() - 1)
            ax |= high_bit
            left ^= high_bit
        # 如果 a & ~mask 更大，则应当全部分给 bx（注意最上面保证了 a>=b）
        bx |= left
        return ax * bx % 1_000_000_007


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/JmhrU1/view/PNf60R/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9+7
        mask = (1<<n)-1
        d = mask&(a^b)
        a = (a-(a&d))|(d^mask)
        b = (b-(b&d))|(d^mask)
        # print(a,b,d)
        def check(aa,bb,dd):
            tot = (aa+bb+dd)
            e = tot//2
            for i in range(n)[::-1]:
                if (dd>>i)&1:
                    if aa|(1<<i) <= e:
                        aa |= (1<<i)
            return aa*(tot-aa)
        ans = max(check(a,b,d),check(b,a,d))        
        return ans%MOD