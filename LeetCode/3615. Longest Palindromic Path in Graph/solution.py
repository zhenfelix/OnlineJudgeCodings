# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # 计算理论最大值
        odd = sum(c % 2 for c in Counter(label).values()) 
        theoretical_max = n - max(odd - 1, 0)  # 奇数选一个放正中心，其余全弃

        if len(edges) == n * (n - 1) // 2:  # 完全图，可以达到理论最大值
            return theoretical_max

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 计算从 x 和 y 向两侧扩展，最多还能访问多少个节点（不算 x 和 y）
        @cache
        def dfs(x: int, y: int, vis: int) -> int:
            res = 0
            for v in g[x]:
                if vis >> v & 1:
                    continue
                for w in g[y]:
                    if vis >> w & 1 == 0 and v != w and label[w] == label[v]:
                        tv, tw = v, w  # 注意不能直接交换 v 和 w，否则下个循环的 v 就不是原来的 v 了
                        if tv > tw:  # 保证 tv < tw，减少状态个数和计算量
                            tv, tw = tw, tv
                        res = max(res, dfs(tv, tw, vis | 1 << v | 1 << w) + 2)
            return res

        ans = 0
        for x, to in enumerate(g):
            # 奇回文串，x 作为回文中心
            ans = max(ans, dfs(x, x, 1 << x) + 1)
            if ans == theoretical_max:
                return ans
            # 偶回文串，x 和 x 的邻居 y 作为回文中心
            for y in to:
                # 保证递归参数 x < y，减少状态个数和计算量
                if x < y and label[x] == label[y]:
                    ans = max(ans, dfs(x, y, 1 << x | 1 << y) + 2)
                    if ans == theoretical_max:
                        return ans
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/longest-palindromic-path-in-graph/solutions/3722469/zhong-xin-kuo-zhan-fa-zhuang-ya-dp-by-en-ai9s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。