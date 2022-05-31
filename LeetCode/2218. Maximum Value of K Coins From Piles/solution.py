class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        n = len(piles)
        dp = [[-float('inf')]*(K+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(n):
            m = len(piles[i])
            s = [0]*(m+1)
            for j in range(1,m+1):
                s[j] = s[j-1]+piles[i][j-1]
            for j in range(1,K+1):
                dp[i+1][j] = max(dp[i][j-k]+s[k] for k in range(min(j,m)+1))
        return dp[-1][-1]


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f = [0] * (k + 1)
        sum_n = 0
        for pile in piles:
            n = len(pile)
            for i in range(1, n):
                pile[i] += pile[i - 1]  # pile 前缀和
            sum_n = min(sum_n + n, k)  # 优化：j 从前 i 个栈的大小之和开始枚举（不超过 k）
            for j in range(sum_n, 0, -1):
                f[j] = max(f[j], max(f[j - w - 1] + pile[w] for w in range(min(n, j))))
        return f[k]


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/maximum-value-of-k-coins-from-piles/solution/zhuan-hua-cheng-fen-zu-bei-bao-pythongoc-3xnk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。