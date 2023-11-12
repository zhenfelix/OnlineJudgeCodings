nmax = 10**5+10
p = [1]*nmax
p[1] = 0
for i in range(2,nmax):
    if not p[i]: continue
    for j in range(i*i,nmax,i):
        p[j] = 0

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        down = [0]*(n+1)
        up = [0]*(n+1)
        ans = 0
        def dfs(cur,pre):
            nonlocal ans
            s = 1
            for nxt in g[cur]:
                if nxt == pre: continue
                dfs(nxt,cur)
                if p[nxt] == 0:
                    down[cur] += down[nxt]+1
                    if p[cur] == 1:
                        ans += (down[nxt]+1)*s 
                        s += down[nxt]+1
            return 
        def reroot(cur,pre):
            nonlocal ans
            if p[cur] == 1:
                ans += up[cur]*(down[cur]+1)
            for nxt in g[cur]:
                if nxt == pre: continue
                if p[cur] == 0:
                    up[nxt] = up[cur]+1+down[cur]-(0 if p[nxt] == 1 else down[nxt]+1)
                reroot(nxt,cur)
            return
        dfs(1,0)
        reroot(1,0)
        # print(down,up)
        return ans 


# 标记 10**5 以内的质数
MX = 10 ** 5 + 1
is_prime = [True] * MX
is_prime[1] = False
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> None:
            nodes.append(x)
            for y in g[x]:
                if y != fa and not is_prime[y]:
                    dfs(y, x)

        ans = 0
        size = [0] * (n + 1)
        for x in range(1, n + 1):
            if not is_prime[x]:  # 跳过非质数
                continue
            s = 0
            for y in g[x]:  # 质数 x 把这棵树分成了若干个连通块
                if is_prime[y]:
                    continue
                if size[y] == 0:  # 尚未计算过
                    nodes = []
                    dfs(y, -1)  # 遍历 y 所在连通块，在不经过质数的前提下，统计有多少个非质数
                    for z in nodes:
                        size[z] = len(nodes)
                # 这 size[y] 个非质数与之前遍历到的 s 个非质数，两两之间的路径只包含质数 x
                ans += size[y] * s
                s += size[y]
            ans += s  # 从 x 出发的路径
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/WhhMVw/view/h8u9cM/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。