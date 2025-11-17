class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[par[i]].append(i)

        qs = [[] for _ in range(n)]
        for i, (x, k) in enumerate(queries):
            qs[x].append((k, i))

        ans = [-1] * len(queries)

        def dfs(x: int, xor: int) -> SortedSet:
            xor ^= vals[x]

            st = SortedSet()
            st.add(xor)
            for y in g[x]:
                set_y = dfs(y, xor)
                # 启发式合并：小集合并入大集合
                if len(set_y) > len(st):
                    st, set_y = set_y, st
                for v in set_y:
                    st.add(v)

            for k, qi in qs[x]:
                if k - 1 < len(st):
                    ans[qi] = st[k - 1]

            return st

        dfs(0, 0)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/kth-smallest-path-xor-sum/solutions/3705587/chi-xian-qi-fa-shi-he-bing-you-xu-ji-he-pm0km/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。