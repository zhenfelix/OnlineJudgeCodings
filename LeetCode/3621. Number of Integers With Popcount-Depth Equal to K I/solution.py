class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        # 注：也可以不转成字符串，下面 dfs 用位运算取出 n 的第 i 位
        # 但转成字符串的通用性更好
        s = list(map(int, bin(n)[2:]))
        m = len(s)
        if k == 1:
            return m - 1

        @cache
        def dfs(i: int, left1: int, is_limit: bool) -> int:
            if i == m:
                return 0 if left1 else 1
            up = s[i] if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        f = [0] * (m + 1)
        for i in range(1, m + 1):
            f[i] = f[i.bit_count()] + 1
            if f[i] == k:
                # 计算有多少个二进制数恰好有 i 个 1
                ans += dfs(0, i, True)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/number-of-integers-with-popcount-depth-equal-to-k-i/solutions/3728362/shu-wei-dpzuo-fa-tong-3352-ti-pythonjava-fjti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。