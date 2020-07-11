class Solution:
    def numSubmat(self, dp: List[List[int]]) -> int:
        sums, n, m = 0, len(dp), len(dp[0])
        cnt = [[0]*m for _ in range(n)]
        sts = [[] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                dp[i][j] += dp[i][j-1]*dp[i][j] if j > 0 else 0
                while sts[j] and dp[sts[j][-1]][j] >= dp[i][j]:
                    sts[j].pop() 
                pre, precnt = -1, 0
                if sts[j]:
                    pre, precnt = sts[j][-1], cnt[sts[j][-1]][j]
                cnt[i][j] += precnt + (i-pre)*dp[i][j]
                sums += cnt[i][j]
                sts[j].append(i)
                # print(i,j,cnt[i][j],dp[i][j])

        return sums


# class Solution:
#     def numSubmat(self, dp: List[List[int]]) -> int:
#         sums, n, m = 0, len(dp), len(dp[0])
#         for i in range(n):
#             for j in range(m):
#                 if dp[i][j]:
#                     dp[i][j] += dp[i][j-1] if j > 0 else 0
#                     w = m
#                     for k in range(i+1)[::-1]:
#                         w = min(w, dp[k][j])
#                         sums += w 
#         return sums