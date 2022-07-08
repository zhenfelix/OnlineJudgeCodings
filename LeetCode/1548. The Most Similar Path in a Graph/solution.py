class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        dp = [1 if names[i] != targetPath[0] else 0 for i in range(n)] 
        k = len(targetPath)
        parent = [[-1]*n for _ in range(k)]
        for i in range(1,k):
            cur = targetPath[i]
            ndp = [float('inf')]*n 
            for a, b in roads:
                if dp[a]+(names[b] != cur) < ndp[b]:
                    ndp[b] = dp[a]+(names[b] != cur)
                    parent[i][b] = a 
                if dp[b]+(names[a] != cur) < ndp[a]:
                    ndp[a] = dp[b]+(names[a] != cur)
                    parent[i][a] = b 
            dp = ndp
            # print(parent[i])
        cur = 0
        for i in range(n):
            if dp[i] < dp[cur]:
                cur = i 
        ans = [cur]
        for i in range(k-1)[::-1]:
            cur = parent[i+1][cur]
            ans.append(cur)
        return ans[::-1]

