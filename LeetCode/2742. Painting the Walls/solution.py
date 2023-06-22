class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache  # 记忆化搜索
        def dfs(i: int, j: int) -> int:  # j 表示剩余需要的体积
            if j <= 0: return 0  # 没有约束：后面什么也不用选了
            if i < 0: return inf  # 此时 j>0，但没有物品可选，不合法
            return min(dfs(i - 1, j - time[i] - 1) + cost[i], dfs(i - 1, j))
        n = len(cost)
        return dfs(n - 1, n)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/painting-the-walls/solution/xuan-huo-bu-xuan-de-dian-xing-si-lu-by-e-ulcd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。