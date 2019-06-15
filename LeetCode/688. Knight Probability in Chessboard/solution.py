# class Solution:
#     def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
#         prob = [[1 for i in range(N)] for j in range(N)]
#         next_i = [1,1,2,2,-1,-1,-2,-2]
#         next_j = [2,-2,1,-1,2,-2,1,-1]
#         for k in range(K):
#             next_prob = [[0 for i in range(N)] for j in range(N)]
#             for i in range(N):
#                 for j in range(N):
#                     for k in range(8):
#                         ii = next_i[k]+i
#                         if ii>=N or ii<0:
#                             continue
#                         jj = next_j[k]+j
#                         if jj>=N or jj<0:
#                             continue
#                         next_prob[i][j] = next_prob[i][j]+0.125*prob[ii][jj]
#             prob = next_prob
#         return prob[r][c]


class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))

