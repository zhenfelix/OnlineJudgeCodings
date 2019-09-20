# class TicTacToe(object):

#     def __init__(self, n):
#         """
#         Initialize your data structure here.
#         :type n: int
#         """
#         self.n = n
#         self.board = [['?']*n for _ in range(n)]
#         self.symbol = ['?','X','O']

#     def move(self, row, col, player):
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         :type row: int
#         :type col: int
#         :type player: int
#         :rtype: int
#         """
#         self.board[row][col] = self.symbol[player]
#         # print(self.board)
#         n = self.n
#         flag = [True, True, row == col, row + col == n-1]
#         for i in range(n):
#             if flag[0] and self.board[i][col] != self.symbol[player]:
#                 flag[0] = False
#             if flag[1] and self.board[row][i] != self.symbol[player]:
#                 flag[1] = False
#             if flag[2] and self.board[i][i] != self.symbol[player]:
#                 flag[2] = False
#             if flag[3] and self.board[n-1-i][i] != self.symbol[player]:
#                 flag[3] = False
                
#         if (True in flag):
#             return player
#         else:
#             return 0

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        # self.board = [['?']*n for _ in range(n)]
        # self.symbol = ['?','X','O']
        self.rows = [[0]*n for _ in range(2)]
        self.cols = [[0]*n for _ in range(2)]
        self.diag = [0]*2
        self.anti_diag = [0]*2

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # self.board[row][col] = self.symbol[player]
        # print(self.board)
        n = self.n
        self.rows[player-1][row] += 1
        self.cols[player-1][col] += 1
        if row == col:
            self.diag[player-1] += 1
        if row + col == n-1:
            self.anti_diag[player-1] += 1
        if n in [self.rows[player-1][row], self.cols[player-1][col], self.diag[player-1], self.anti_diag[player-1]]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)