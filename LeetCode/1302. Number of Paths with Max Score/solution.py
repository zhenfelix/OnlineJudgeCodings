# class Solution:
#     def pathsWithMaxScore(self, board: List[str]) -> List[int]:
#         n = len(board)
#         board[0] = '0'+board[0][1:]
#         score = [[0]*n for _ in range(n)]
#         path = [[0]*n for _ in range(n)]
#         path[-1][-1] = 1
#         for i in range(n-1)[::-1]:
#             if board[n-1][i] == 'X':
#                 path[n-1][i] = 0
#                 score[n-1][i] = 0
#             elif path[n-1][i+1] > 0:
#                 path[n-1][i] = path[n-1][i+1]
#                 score[n-1][i] = int(board[n-1][i]) + score[n-1][i+1]
#         for i in range(n-1)[::-1]:
#             if board[i][n-1] == 'X':
#                 path[i][n-1] = 0
#                 score[i][n-1] = 0
#             elif path[i+1][n-1] > 0:
#                 path[i][n-1] = path[i+1][n-1]
#                 score[i][n-1] = int(board[i][n-1]) + score[i+1][n-1]

#         for i in range(n-1)[::-1]:
#             for j in range(n-1)[::-1]:
#                 if board[i][j] == 'X':
#                     path[i][j] = 0
#                     score[i][j] = 0
#                 else:
#                     candidates = []
#                     if path[i][j+1] > 0:
#                         candidates.append((score[i][j+1],path[i][j+1]))
#                     if path[i+1][j] > 0:
#                         candidates.append((score[i+1][j],path[i+1][j]))
#                     if path[i+1][j+1] > 0:
#                         candidates.append((score[i+1][j+1],path[i+1][j+1]))
#                     if not candidates:
#                         continue
#                     mx = max(candidate[0] for candidate in candidates)
#                     score[i][j] = mx + int(board[i][j])
#                     for candidate in candidates:
#                         if candidate[0] == mx:
#                             path[i][j] += candidate[1]
                            
#         return [score[0][0]%(10**9+7),path[0][0]%(10**9+7)]


                
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        board[0] = '0'+board[0][1:]
        board[-1] = board[-1][:-1]+'0'
        score = [[0]*(n+1) for _ in range(n+1)]
        path = [[0]*(n+1) for _ in range(n+1)]
        path[-1][-1] = 1
        # for i in range(n-1)[::-1]:
        #     if board[n-1][i] == 'X':
        #         path[n-1][i] = 0
        #         score[n-1][i] = 0
        #     elif path[n-1][i+1] > 0:
        #         path[n-1][i] = path[n-1][i+1]
        #         score[n-1][i] = int(board[n-1][i]) + score[n-1][i+1]
        # for i in range(n-1)[::-1]:
        #     if board[i][n-1] == 'X':
        #         path[i][n-1] = 0
        #         score[i][n-1] = 0
        #     elif path[i+1][n-1] > 0:
        #         path[i][n-1] = path[i+1][n-1]
        #         score[i][n-1] = int(board[i][n-1]) + score[i+1][n-1]

        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if board[i][j] == 'X':
                    path[i][j] = 0
                    score[i][j] = 0
                else:
                    candidates = []
                    candidates.append((score[i][j+1],path[i][j+1]))
                    candidates.append((score[i+1][j],path[i+1][j]))
                    candidates.append((score[i+1][j+1],path[i+1][j+1]))
                    if all(candidate[1] == 0 for candidate in candidates):
                        continue
                    mx = max(candidate[0] for candidate in candidates if candidate[1] > 0)
                    score[i][j] = mx + int(board[i][j])
                    for candidate in candidates:
                        if candidate[0] == mx:
                            path[i][j] += candidate[1]
                            
        return [score[0][0]%(10**9+7),path[0][0]%(10**9+7)]




class Solution:
    def pathsWithMaxScore(self, A):
        n, mod = len(A), 10**9 + 7
        dp = [[[-10**5, 0] for j in range(n + 1)] for i in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]
        for x in range(n)[::-1]:
            for y in range(n)[::-1]:
                if A[x][y] in 'XS': continue
                for i, j in [[0, 1], [1, 0], [1, 1]]:
                    if dp[x][y][0] < dp[x + i][y + j][0]:
                        dp[x][y] = [dp[x + i][y + j][0], 0]
                    if dp[x][y][0] == dp[x + i][y + j][0]:
                        dp[x][y][1] += dp[x + i][y + j][1]
                    # if dp[x][y][0] < dp[x + i][y + j][0]:
                    #     # dp[x][y] = [dp[x + i][y + j][0], dp[x + i][y + j][1]]
                    #     dp[x][y] = dp[x + i][y + j][:]
                    # elif dp[x][y][0] == dp[x + i][y + j][0]:
                    #     dp[x][y][1] += dp[x + i][y + j][1]

                dp[x][y][0] += int(A[x][y]) if x or y else 0
        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % mod]

                
