class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = [[] for _ in range(len(vals))]
        for x, y in edges:
            if vals[y] > 0: g[x].append(vals[y])
            if vals[x] > 0: g[y].append(vals[x])
        return max(v + sum(nlargest(k, a)) for v, a in zip(vals, g))


作者：endlesscheng
链接：https://leetcode.cn/problems/maximum-star-sum-of-a-graph/solution/mei-ju-pai-xu-by-endlesscheng-pblv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        hqs = [[] for _ in range(n)]
        ss = vals.copy()
        for a, b in edges:
            if vals[b] > 0:
                heappush(hqs[a], vals[b])
                ss[a] += vals[b]
                if len(hqs[a]) > k:
                    v = heappop(hqs[a])
                    ss[a] -= v 
            if vals[a] > 0:
                heappush(hqs[b], vals[a])
                ss[b] += vals[a]
                if len(hqs[b]) > k:
                    v = heappop(hqs[b])
                    ss[b] -= v 
        return max(ss)