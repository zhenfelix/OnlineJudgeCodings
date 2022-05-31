class Solution:
    def lightSticks(self, height: int, width: int, indices: List[int]) -> List[int]:
        tot = (height+1)*(width+1)
        indices = set(indices)
        graph = defaultdict(list)
        e = 0
        for r in range(height+1):
            for c in range(width+1):
                cur = r*(width+1)+c
                if r > 0:
                    pre = (r-1)*(width+1)+c
                    if e not in indices:
                        graph[cur].append(pre)
                        graph[pre].append(cur)
                    e += 1
            for c in range(width+1):
                cur = r*(width+1)+c 
                if c > 0:
                    pre = r*(width+1)+c-1
                    if e not in indices:
                        graph[cur].append(pre)
                        graph[pre].append(cur)
                    e += 1
        # print(e)
        connected = sum(len(graph[i]) > 0 for i in range(tot))
        def bfs(pos):
            cur = [pos]
            visited = [False]*tot
            visited[pos] = True
            cnt = 1
            dist = 0
            while cur:
                nxt = []
                for i in cur:
                    for j in graph[i]:
                        if not visited[j]:
                            visited[j] = True
                            cnt += 1
                            nxt.append(j)
                cur = nxt
                dist += 1
            return cnt, dist

        ans, best = [], float('inf')
        for i in range(tot):
            if len(graph[i]) == 0:
                continue
            cnt, dist = bfs(i)
            if cnt < connected:
                return []
            if dist < best:
                ans = [i]
                best = dist
            elif dist == best:
                ans.append(i)
        return ans
