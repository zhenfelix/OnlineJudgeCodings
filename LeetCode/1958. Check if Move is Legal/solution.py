class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n, m = len(board), len(board[0])
        def judge(r,c,dr,dc,ch):
            cnt = 1
            while 0 <= r+dr < n and 0 <= c+dc < m:
                r += dr
                c += dc
                cnt += 1
                if board[r][c] == '.':
                    return False
                if board[r][c] == ch:
                    return cnt >= 3
            return False
        return any(judge(rMove,cMove,dr,dc,color) for dr,dc in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)])