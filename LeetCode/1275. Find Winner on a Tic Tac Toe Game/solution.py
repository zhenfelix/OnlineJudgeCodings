class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def judge(r,c):
            flag = False
            flag = flag or all([grid[i][c] == grid[r][c] for i in range(3)])
            flag = flag or all([grid[r][j] == grid[r][c] for j in range(3)])
            flag = flag or all([r==c]+[grid[i][i] == grid[r][c] for i in range(3)])
            flag = flag or all([r+c == 2]+[grid[i][2-i] == grid[r][c] for i in range(3)])
            return flag

        grid = [[" "]*3 for _ in range(3)]
        for idx, move in enumerate(moves):
            r, c = move[0], move[1]
            if idx%2 == 0:
                grid[r][c] = 'X'
            else:
                grid[r][c] = 'O'
        row, col = moves[-1][0], moves[-1][-1]
        if judge(row, col):
            if grid[row][col] == 'X':
                return 'A'
            else:
                return 'B'
        if len(moves) == 9:
            return "Draw"
        return "Pending"