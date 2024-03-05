class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [1] * n
        def dfs(x: int, fa: int) -> List[int]:
            a = [cost[x]]
            for y in g[x]:
                if y != fa:
                    a.extend(dfs(y, x))
            a.sort()
            m = len(a)
            if m >= 3:
                ans[x] = max(a[-3] * a[-2] * a[-1], a[0] * a[1] * a[-1], 0)
            if m > 5:
                a = a[:2] + a[-3:]
            return a
        dfs(0, -1)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-number-of-coins-to-place-in-tree-nodes/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        coin = [1]*n 

        def dfs(cur,pre):
            pos = []
            neg = []
            if cost[cur] > 0:
                pos.append(cost[cur])
            else:
                neg.append(-cost[cur])
            for nxt in g[cur]:
                if pre == nxt: continue 
                tmp_pos, tmp_neg = dfs(nxt,cur)
                for v in tmp_pos:
                    heappush(pos,v)
                    if len(pos) > 3:
                        heappop(pos)
                for v in tmp_neg:
                    heappush(neg,v)
                    if len(neg) > 3:
                        heappop(neg)
            ans = 0
            if len(pos)+len(neg) < 3:
                ans = 1
            else:
                if len(pos) >= 3:
                    tmp = 1
                    for v in pos:
                        tmp *= v  
                    ans = max(ans,tmp)
                if len(neg) >= 2 and pos:
                    tmp = 1
                    if len(neg) > 2:
                        heappop(neg)
                    for v in neg:
                        tmp *= -v 
                    tmp *= max(pos)
                    ans = max(ans,tmp)
            coin[cur] = ans 
            return pos,neg  
        dfs(0,0)
        return coin 