class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        def nxt(cur):
            if cur > int(cur)+0.000000001:
                return int(cur)+1
            return cur

        n = len(dist)
        dp = [[10**8]*n for _ in range(n)]
        for i in range(n):
            pre = nxt(dp[i-1][0]) if i else 0
            dp[i][0] = pre + dist[i]/speed
        if dp[n-1][0] <= hoursBefore:
            return 0
        for j in range(1,n):
            for i in range(j,n):
                pre = nxt(dp[i-1][j])
                dp[i][j] = min(dp[i][j], pre + dist[i]/speed)
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist[i]/speed)
            if dp[n-1][j] <= hoursBefore:
                return j
        # print(dp)
        return -1




class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        def nxt(cur):
            if cur%speed:
                return cur-(cur%speed)+speed
            return cur

        n = len(dist)
        dist = [d*speed for d in dist]
        hoursBefore *= speed
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            pre = nxt(dp[i-1][0]) if i else 0
            dp[i][0] = pre + dist[i]//speed
        if dp[n-1][0] <= hoursBefore:
            return 0
        for j in range(1,n):
            for i in range(j,n):
                pre = nxt(dp[i-1][j])
                dp[i][j] = min(dp[i][j], pre + dist[i]//speed)
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist[i]//speed)
            if dp[n-1][j] <= hoursBefore:
                return j
        # print(dp)
        return -1

