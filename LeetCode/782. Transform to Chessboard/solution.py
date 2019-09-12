class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)):
            return -1
        if not n//2 <= sum(board[0]) <= (n+1)//2:
            return -1
        if not n//2 <= sum(board[i][0] for i in range(n)) <= (n+1)//2:
            return -1
        cols = sum(board[0][j] == j%2 for j in range(n))
        rows = sum(board[i][0] == i%2 for i in range(n)) 
        if n%2:
            if cols%2:
                cols = n - cols
            if rows%2:
                rows = n - rows
        else:
            cols = min(cols, n-cols)
            rows = min(rows, n-rows)
        
        return (rows+cols)//2