class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        def calc(w):
            h = 0
            for ch in w:
                h |= (1<<(ord(ch)-ord('a')))
            return h 

        sz = Counter(map(calc,words))
        candidates = list(sz)
        graph = defaultdict(list)

        def connect(x,y):
            graph[x].append(y)
            graph[y].append(x)

        for x in candidates:
            connect(x,x^(1<<26))
            for i in range(26):
                if (x>>i)&1:
                    connect(x,x^(1<<26)^(1<<i))

        gp, mx = 0, 0
        visited = set()

        def bfs(cur):
            visited.add(cur)
            q = deque([cur])
            cnt = 0
            while q:
                cur = q.popleft()
                cnt += sz[cur]
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            return cnt


        for x in candidates:
            if x not in visited:
                cnt = bfs(x)
                mx = max(mx, cnt)
                gp += 1

        return [gp, mx]




class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        def calc(w):
            h = 0
            for ch in w:
                h |= (1<<(ord(ch)-ord('a')))
            return h 

        sz = Counter(map(calc,words))
        candidates = list(sz)
        parent = dict()
        mx, gp = 1, 0

        def find(r):
            nonlocal gp
            if r not in parent:
                parent[r] = r
                gp += 1
            if parent[r] != r:
                parent[r] = find(parent[r])
            return parent[r]

        def connect(u,v):
            nonlocal mx, gp
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                sz[rv] += sz[ru]
                mx = max(mx, sz[rv])
                gp -= 1
            return 

        for x in candidates:
            connect(x,x^(1<<26))
            for i in range(26):
                if (x>>i)&1:
                    connect(x,x^(1<<26)^(1<<i))
        return [gp, mx]








class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        def calc(w):
            h = 0
            for ch in w:
                h |= (1<<(ord(ch)-ord('a')))
            return h 

        mp = Counter(map(calc,words))
        visited = set()

        def get_adjacent(cur):
            for i in range(26):
                yield cur^(1<<i)
                if (cur>>i)&1:
                    for j in range(26):
                        if not (cur>>j)&1:
                            yield cur^(1<<i)^(1<<j)
            return

        def bfs(cur):
            cnt = 0
            visited.add(h)
            q = deque([cur])
            while q:
                cur = q.popleft()
                cnt += mp[cur]
                for nxt in get_adjacent(cur):
                    if mp[nxt] and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            return cnt


        res = [0,0]
        for h in mp:
            if h not in visited:
                cnt = bfs(h)
                res[0] += 1
                res[1] = max(res[1],cnt)

        return res




class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # 并查集模板（哈希表写法）
        fa, size = {}, defaultdict(int)
        groups, max_size = len(words), 0
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(x: int, y: int):
            nonlocal groups, max_size
            if y not in fa:
                return
            x, y = find(x), find(y)
            if x == y:
                return
            fa[x] = y
            size[y] += size[x]
            max_size = max(max_size, size[y])  # 维护答案
            groups -= 1

        for word in words:
            x = 0
            for ch in word:
                x |= 1 << (ord(ch) - ord('a'))  # 计算 word 的二进制表示
            fa[x] = x  # 添加至并查集
            size[x] += 1
            max_size = max(max_size, size[x])  # 维护答案
            if size[x] > 1:
                groups -= 1

        for x in fa:  # 枚举所有字符串（二进制表示）
            for i in range(26):
                merge(x, x ^ (1 << i))  # 添加或删除字符 i
                if (x >> i) & 1:
                    for j in range(26):
                        if ((x >> j) & 1) == 0:
                            merge(x, x ^ (1 << i) | (1 << j))  # 替换字符 i 为 j
        return [groups, max_size]


作者：endlesscheng
链接：https://leetcode-cn.com/problems/groups-of-strings/solution/bing-cha-ji-wei-yun-suan-by-endlesscheng-uejd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # 使用哈希映射统计每一个二进制表示出现的次数
        wordmasks = Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            wordmasks[mask] += 1
        
        # 辅助函数，用来得到 mask 的所有可能的相邻节点
        def get_adjacent(mask: int) -> List[int]:
            # 将一个 0 变成 1，或将一个 1 变成 0
            for i in range(26):
                yield (mask ^ (1 << i))
            # 将一个 0 变成 1，且将一个 1 变成 0
            for i in range(26):
                if mask & (1 << i):
                    for j in range(26):
                        if not (mask & (1 << j)):
                            yield (mask ^ (1 << i) ^ (1 << j))
            return
        
        used = set()
        best = cnt = 0
        for mask, occ in wordmasks.items():
            if mask in used:
                continue
            
            # 从一个未搜索过的节点开始进行广度优先搜索，并求出对应连通分量的大小
            q = deque([mask])
            used.add(mask)
            # total 记录联通分量的大小
            total = occ

            while q:
                u = q.popleft()
                for v in get_adjacent(u):
                    if v in wordmasks and v not in used:
                        q.append(v)
                        used.add(v)
                        total += wordmasks[v]
            
            best = max(best, total)
            cnt += 1
            
        return [cnt, best]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/groups-of-strings/solution/zi-fu-chuan-fen-zu-by-leetcode-solution-a8dr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。