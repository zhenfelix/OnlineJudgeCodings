class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        n, m = destination
        n, m = n+1, m+1
        dp = [[0]*m for _ in range(n)]
        dp[-1][-1] = 1
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                if i + 1 < n:
                    dp[i][j] += dp[i+1][j]
                if j + 1 < m:
                    dp[i][j] += dp[i][j+1]
        # print(dp)
        cur, i, j = '', 0, 0
        for _ in range(n+m-2):
            if j + 1 < m and dp[i][j+1] >= k :
                j += 1
                cur += 'H'
            else:
                if j + 1 < m:
                    k -= dp[i][j+1]
                i += 1
                cur += 'V'

        return cur

    # def kthSmallestPath(self, destination: List[int], k: int) -> str:
    #         from math import comb
    #         r, c = destination
            
    #         ret = []
    #         remDown = r
    #         for i in range(r + c):
    #             remSteps = r + c - (i + 1)
    #             com = comb(remSteps, remDown)
    #             if com >= k:
    #                 ret.append("H")
    #             else:
    #                 remDown -= 1
    #                 k -= com
    #                 ret.append("V")
                    
    #         return ''.join(ret)