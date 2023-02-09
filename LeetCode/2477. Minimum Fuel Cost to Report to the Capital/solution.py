class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = defaultdict(list)
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)

        def dfs(cur, parent):
            cost, cnt = 0, 1
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                ncost, ncnt = dfs(nxt, cur)
                cost += ncost+(ncnt-1)//seats+1
                cnt += ncnt
            return cost, cnt 
        oil, _ = dfs(0,0)
        return oil

class Solution:

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        ans = 0

        g = [[] for _ in range(len(roads) + 1)]

        for x, y in roads:

            g[x].append(y)

            g[y].append(x)

        def dfs(x: int, fa: int) -> int:

            size = 1

            for y in g[x]:

                if y != fa:

                    size += dfs(y, x)

            if x:

                nonlocal ans

                ans += (size + seats - 1) // seats

            return size

        dfs(0, -1)

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/solutions/1981361/kao-lu-mei-tiao-bian-shang-zhi-shao-xu-y-uamv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。