class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegree = [0]*n
        graph = defaultdict(list)
        dp = [[0]*26 for _ in range(n)]
        res = 0
        for a, b in edges:
            indegree[b] += 1
            graph[a].append(b)
        q = deque()
        visited = set()
        for i in range(n):
            if indegree[i] == 0:
                visited.add(i)
                q.append(i)
                dp[i][ord(colors[i])-ord('a')] += 1
                res = max(res, dp[i][ord(colors[i])-ord('a')])
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                for i in range(26):
                    dp[nxt][i] = max(dp[nxt][i], dp[cur][i]+1 if i == ord(colors[nxt])-ord('a') else dp[cur][i])
                    res = max(res, dp[nxt][i])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    visited.add(nxt)
                    q.append(nxt)
                    
                    
                    
        # print(dp)
        if len(visited) == n:
            return res
        return -1



