class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def calc(arr):
            indegree = Counter()
            g = defaultdict(list)
            for a, b in arr:
                g[a].append(b)
                indegree[b] += 1
            q = deque()
            ans = []
            for i in range(1,k+1):
                if indegree[i] == 0:
                    q.append(i)
                    ans.append(i)
            while q:
                cur = q.popleft()
                for nxt in g[cur]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
                        ans.append(nxt)
            return ans
        # n, m = len(rowConditions), len(colConditions)
        rows = calc(rowConditions)[:]
        cols = calc(colConditions)[:]
        # print(rows,cols)
        if len(rows) < k or len(cols) < k:
            return []
        posx = dict()
        posy = dict()
        for i, v in enumerate(rows):
            posx[v] = i
        for i, v in enumerate(cols):
            posy[v] = i 
        res = [[0]*k for _ in range(k)]
        for v in range(1,k+1):
            res[posx[v]][posy[v]] = v  
        return res 

