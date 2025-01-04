class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))

        def dfs(x: int, fa: int) -> Tuple[int, int]:
            not_choose = 0
            inc = []
            for y, wt in g[x]:
                if y == fa:
                    continue
                nc, c = dfs(y, x)
                not_choose += nc  # 先都不选
                if (d := c + wt - nc) > 0:
                    inc.append(d)
            inc.sort(reverse=True)
            # 再选增量最大的 k 个或者 k-1 个
            return not_choose + sum(inc[:k]), not_choose + sum(inc[:k - 1])
        return max(dfs(0, -1))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-sum-of-weights-after-edge-removals/solutions/2998845/shu-xing-dp-tan-xin-pythonjavacgo-by-end-i3g3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。