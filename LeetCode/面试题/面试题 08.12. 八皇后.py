class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(path):
            nonlocal res
            if len(path) == n:
                res.append(path)
                return 
            for j in range(n):
                if path and any(c==j or len(path)-j==r-c or len(path)+j==r+c for r, c in enumerate(path)):
                    continue
                dfs(path+[j])
            return 

        def func(path):
            board = []
            for j in path:
                board.append('.'*j+'Q'+'.'*(n-j-1))
            return board

        dfs([])
        
        return list(map(func,res))