class Solution:
    def maximizeTheProfit(self, m: int, offers: List[List[int]]) -> int:
        n = len(offers)
        offers.sort(key = lambda x: x[1])
        ends = [x[1] for x in offers]
        dp = [0]*(n+1)
        for i in range(n):
            s, e, g = offers[i]
            j = bisect.bisect_left(ends,s)-1
            dp[i] = max(dp[i-1],dp[j]+g)
            # print(dp[i],j)
        return dp[n-1]


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        groups = [[] for _ in range(n)]
        for start, end, gold in offers:
            groups[end].append((start, gold))
        f = [0] * (n + 1)
        for end, g in enumerate(groups):
            f[end + 1] = f[end]
            for start, gold in g:
                f[end + 1] = max(f[end + 1], f[start] + gold)
        return f[n]


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/SIJedb/view/ZVZvhi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。