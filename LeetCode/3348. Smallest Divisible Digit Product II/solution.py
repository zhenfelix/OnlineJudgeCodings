class Solution:
    def smallestNumber(self, s: str, t: int) -> str:
        tmp = t
        cnt = 0
        for p in 2, 3, 5, 7:
            while tmp % p == 0:
                tmp //= p
                cnt += 1
        if tmp > 1:  # t 包含其他质因子
            return "-1"

        # 补前导零（至少一个）
        cnt = max(cnt - len(s) + 1, 1)
        s = '0' * cnt + s

        n = len(s)
        ans = [0] * n

        @cache  # 仅仅作为 vis 标记使用
        def dfs(i: int, t: int, is_limit: bool) -> bool:
            if i == n:
                return t == 1

            x = int(s[i])
            # 如果没有约束，那么 1~9 随便填（注意这意味着前面填了大于 0 的数）
            low = x if is_limit and (x or i < cnt) else 1
            for d in range(low, 10):
                ans[i] = d  # 直接覆盖，无需恢复现场
                new_t = t // gcd(t, d) if d > 1 else t
                if dfs(i + 1, new_t, is_limit and d == x):
                    return True
            return False

        dfs(0, t, True)
        dfs.cache_clear()  # 防止爆内存
        return ''.join(map(str, ans)).lstrip('0')  # 去掉前导零

作者：灵茶山艾府
链接：https://leetcode.cn/problems/smallest-divisible-digit-product-ii/solutions/2984014/bao-sou-zuo-fa-lei-si-shu-wei-dp-by-endl-nkoo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。