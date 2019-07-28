# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         ans = []
        
#         def dfs(path, bd):
#             if len(path) == n:
#                 ans.append(bd)
#                 return
            
#             for col in range(n):
#                 flag = True
#                 for row, p in enumerate(path):
#                     if col == p or abs(col-p) == len(path)-row:
#                         flag = False
#                         break
#                 if flag:
#                     sym = "."*col+"Q"+"."*(n-col-1)
#                     dfs(path+[col],bd+[sym])
#             return
#         dfs([],[])
#         return ans


class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]