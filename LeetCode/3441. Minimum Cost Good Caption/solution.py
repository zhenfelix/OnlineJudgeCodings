class Solution:
    def minCostGoodCaption(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return ""

        s = [ord(c) - ord('a') for c in s]
        f = [[0] * 26 for _ in range(n + 1)]
        min_j = [0] * (n + 1)
        nxt = [[0] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            mn = inf
            for j in range(26):
                res = f[i + 1][j] + abs(s[i] - j)
                res2 = f[i + 3][min_j[i + 3]] + abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j) if i <= n - 6 else inf
                if res2 < res or res2 == res and min_j[i + 3] < j:
                    res = res2
                    nxt[i][j] = min_j[i + 3]  # 记录转移来源
                else:
                    nxt[i][j] = j  # 记录转移来源
                f[i][j] = res
                if res < mn:
                    mn = res
                    min_j[i] = j  # 记录最小的 f[i][j] 中的 j 是多少

        ans = [''] * n
        i, j = 0, min_j[0]
        while i < n:
            ans[i] = ascii_lowercase[j]
            k = nxt[i][j]
            if k == j:
                i += 1
            else:
                ans[i + 2] = ans[i + 1] = ans[i]
                i += 3
                j = k
        return ''.join(ans)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-good-caption/solutions/3061609/zhuang-tai-ji-dp-shu-chu-ju-ti-fang-an-p-kjry/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。