from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        q = deque()
        visited = set()
        q.append((click[0],click[1]))
        visited.add((click[0],click[1]))
        while  q:
            x, y = q.popleft()
            if board[x][y] == 'M':
                board[x][y] = 'X'
                break
            cc = 0
            for i in range(x-1,x+2,1):
                for j in range(y-1,y+2,1):
                    if i >= 0 and i < n and j >= 0 and j < m and board[i][j] == 'M':
                        cc += 1
            if cc == 0:
                board[x][y] = 'B'
                for i in range(x-1,x+2,1):
                    for j in range(y-1,y+2,1):
                        if i >= 0 and i < n and j >= 0 and j < m and (i,j) not in visited:
                            q.append((i,j))
                            visited.add((i,j))
            else:
                board[x][y] = str(cc)
        return board


