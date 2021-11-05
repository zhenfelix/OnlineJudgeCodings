class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dp = [0]*n 
        degree = [0]*n 
        graph = defaultdict(list)
        for a, b in relations:
            a -= 1
            b -= 1
            graph[a].append(b)
            degree[b] += 1
        q = deque()
        for a in range(n):
            if degree[a] == 0:
                q.append(a)
                dp[a] = time[a]
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                dp[nxt] = max(dp[nxt], dp[cur]+time[nxt])
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        return max(dp)

