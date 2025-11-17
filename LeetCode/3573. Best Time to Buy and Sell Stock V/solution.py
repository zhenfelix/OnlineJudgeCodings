class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        n = len(prices)
        g1 = [p for p in prices]
        g2 = [-p for p in prices]
        for i in range(1,n):
            g1[i] = max(g1[i],g1[i-1])
            g2[i] = max(g2[i],g2[i-1])
        f = [0]*n  
        ng1 = g1[:]
        ng2 = g2[:]
        for _ in range(k):
            for i in range(n):
                if i > 0:
                    f[i] = max(f[i-1],-prices[i]+g1[i-1],prices[i]+g2[i-1])
                if i < n-1:
                    ng1[i+1] = max(ng1[i],prices[i+1]+f[i])
                    ng2[i+1] = max(ng2[i],-prices[i+1]+f[i])
            g1, g2, ng1, ng2 = ng1, ng2, g1, g2
        return f[-1]


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # 在 [0,i] 中完成至多 j 笔交易，第 i 天结束时的状态为 end_state 的情况下的最大收益
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, end_state: int) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if end_state else 0
            p = prices[i]
            if end_state == 0:
                return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
            if end_state == 1:
                return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)
        ans = dfs(len(prices) - 1, k, 0)
        dfs.cache_clear()  # 防止爆内存（一般来说，状态数达到 1e6 就需要写这个）
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-v/solutions/3695611/zhuang-tai-ji-dpzai-188-ti-de-ji-chu-sha-aozb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。