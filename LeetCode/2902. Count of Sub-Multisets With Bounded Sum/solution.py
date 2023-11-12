class Solution:

    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:

        MOD = 10 ** 9 + 7

        total = sum(nums)

        if l > total:

            return 0



        r = min(r, total)

        cnt = Counter(nums)

        f = [cnt[0] + 1] + [0] * r

        del cnt[0]



        s = 0

        for x, c in cnt.items():

            new_f = f.copy()

            s = min(s + x * c, r)  # 到目前为止，能选的元素和至多为 s

            for j in range(x, s + 1):  # 把循环上界从 r 改成 s，能快一倍

                new_f[j] += new_f[j - x]

                if j >= (c + 1) * x:

                    new_f[j] -= f[j - (c + 1) * x]

                new_f[j] %= MOD

            f = new_f

        return sum(f[l:]) % MOD

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-of-sub-multisets-with-bounded-sum/solutions/2482876/duo-zhong-bei-bao-fang-an-shu-cong-po-su-f5ay/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:

    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:

        MOD = 10 ** 9 + 7

        total = sum(nums)

        if l > total:

            return 0



        r = min(r, total)

        cnt = Counter(nums)

        f = [cnt[0] + 1] + [0] * r

        del cnt[0]



        s = 0

        for x, c in cnt.items():

            s = min(s + x * c, r)

            for j in range(x, s + 1):

                f[j] = (f[j] + f[j - x]) % MOD  # 原地计算同余前缀和

            for j in range(s, (c + 1) * x - 1, -1):

                f[j] = (f[j] - f[j - (c + 1) * x]) % MOD  # 两个同余前缀和的差

        return sum(f[l:]) % MOD

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-of-sub-multisets-with-bounded-sum/solutions/2482876/duo-zhong-bei-bao-fang-an-shu-cong-po-su-f5ay/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。