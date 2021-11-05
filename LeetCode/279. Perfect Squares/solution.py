class Solution:
    def numSquares(self, target: int) -> int:
        sq = []
        cur = 1
        while cur*cur <= target:
            sq.append(cur*cur)
            cur += 1
        q = deque()
        q.append(0)
        step = 0
        visited = [False]*(target+1)
        visited[0] = True
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur == target:
                    return step
                for nxt in sq:
                    if cur+nxt > target:
                        break
                    if visited[cur+nxt]:
                        continue
                    visited[cur+nxt] = True
                    q.append(cur+nxt)
            step += 1
        return -1


# class Solution:
#     def numSquares(self, n: int) -> int:
#         @lru_cache(None)
#         def dfs(i, target):
#             if target == 0:
#                 return 0
#             if i*i > target:
#                 return float('inf')
#             return min(dfs(i, target-i*i)+1, dfs(i+1, target))
#         return dfs(1, n)


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        sq = int(sqrt(n))
        for i in range(1,sq+1)[::-1]:
            for t in range(1,n+1):
                if i*i > t:
                    continue
                dp[t] = min(dp[t], dp[t-i*i]+1)
        return dp[-1]