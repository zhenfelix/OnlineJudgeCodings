dxy = [[0,1],[0,-1],[1,0],[-1,0]]

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def check(r,c,dr,dc):
            for ch in word:
                if 0 <= r < n and 0 <= c < m and (board[r][c] == ch or board[r][c] == " "):
                    r += dr
                    c += dc
                    continue
                return False
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] == "#":
                return True
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    continue
                for dx, dy in dxy:
                    x = i-dx
                    y = j-dy
                    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == "#":
                        if check(i,j,dx,dy):
                            return True
        return False