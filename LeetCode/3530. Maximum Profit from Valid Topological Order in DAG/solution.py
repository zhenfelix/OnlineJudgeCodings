class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        if not edges:
            score.sort()
            return sum(s * i for i, s in enumerate(score, 1))

        # 记录每个节点的先修课（直接前驱）
        pre = [0] * n
        for x, y in edges:
            pre[y] |= 1 << x

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(s: int) -> int:
            res = 0
            i = s.bit_count() + 1  # 已学课程数加一
            # 枚举还没学过的课程 j，且 j 的所有先修课都学完了
            for j, p in enumerate(pre):
                if (s >> j & 1) == 0 and (s | p) == s:
                    r = dfs(s | 1 << j) + score[j] * i
                    if r > res:  # 手写 max
                        res = r
            return res

        return dfs(0)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-profit-from-valid-topological-order-in-dag/solutions/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。