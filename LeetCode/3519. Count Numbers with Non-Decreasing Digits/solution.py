class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def trans(s: str) -> List[int]:
            x = int(s)
            digits = []
            while x:
                x, r = divmod(x, b)
                digits.append(r)
            digits.reverse()
            return digits

        high = trans(r)
        n = len(high)
        low = trans(l)
        low = [0] * (n - len(low)) + low

        @cache
        def dfs(i: int, pre: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else b - 1

            res = 0
            for d in range(max(lo, pre), hi + 1):
                res += dfs(i + 1, d, limit_low and d == lo, limit_high and d == hi)
            return res % 1_000_000_007

        return dfs(0, 0, True, True)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-numbers-with-non-decreasing-digits/solutions/3649556/mo-ban-shang-xia-jie-shu-wei-dp-by-endle-rhuw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。