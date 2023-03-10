class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        mx = [0]*n 
        mx2 = [0]*n 
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(cur, parent):
            for nxt in g[cur]:
                if nxt == parent: continue
                dfs(nxt, cur)
                if mx[nxt]+price[nxt] > mx[cur]:
                    mx[cur], mx2[cur] = mx[nxt]+price[nxt], mx[cur]
                elif mx[nxt]+price[nxt] > mx2[cur]:
                    mx2[cur] = mx[nxt]+price[nxt]
            return  

        dfs(0,0)
        # print(mx,mx2)
        ans = 0
        def dfs2(cur, parent, up):
            nonlocal ans 
            ans = max(ans, up, mx[cur])
            for nxt in g[cur]:
                if nxt == parent: continue
                if mx[nxt]+price[nxt] == mx[cur]:
                    dfs2(nxt,cur,max(up,mx2[cur])+price[cur])
                else:
                    dfs2(nxt,cur,max(up,mx[cur])+price[cur])
            return
        dfs2(0,0,0)
        return ans 





class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树

        ans = 0
        # 返回带叶子的最大路径和，不带叶子的最大路径和
        def dfs(x: int, fa: int) -> (int, int):
            nonlocal ans
            max_s1 = p = price[x]
            max_s2 = 0
            for y in g[x]:
                if y == fa: continue
                s1, s2 = dfs(y, x)
                # 前面最大带叶子的路径和 + 当前不带叶子的路径和
                # 前面最大不带叶子的路径和 + 当前带叶子的路径和
                ans = max(ans, max_s1 + s2, max_s2 + s1)
                max_s1 = max(max_s1, s1 + p)
                max_s2 = max(max_s2, s2 + p)  # 这里加上 p 是因为 x 必然不是叶子
            return max_s1, max_s2
        dfs(0, -1)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/solution/by-endlesscheng-5l70/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。