# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         mp = defaultdict(list)
#         rows, cols = [0]*n, [0]*m 
#         answer = [[0]*m for _ in range(n)]
#         parent = [i*m+j for i in range(n) for j in range(m)]
#         def find(cur):
#             if parent[cur] != cur:
#                 parent[cur] = find(parent[cur])
#             return parent[cur]
#         def union(a,b):
#             ra, rb = find(a), find(b)
#             if ra != rb:
#                 parent[ra] = rb
#             return

#         for i in range(n):
#             for j in range(m):
#                 for r in range(i+1,n):
#                     if matrix[i][j] == matrix[r][j]:
#                         union(i*m+j,r*m+j)
#                 for c in range(j+1,m):
#                     if matrix[i][j] == matrix[i][c]:
#                         union(i*m+j,i*m+c)
#         for i in range(n):
#             for j in range(m):
#                 mp[matrix[i][j],find(i*m+j)].append((i,j))

#         for k in sorted(mp):
#             v = mp[k]
#             rank = max(max(answer[i][j],rows[i]+1,cols[j]+1) for i, j in v)
#             for i, j in v:
#                 answer[i][j] = rank 
#                 rows[i] = rank
#                 cols[j] = rank 
          
#         return answer

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        mp = defaultdict(list)
        row_seen, col_seen = defaultdict(list), defaultdict(list)
        rows, cols = [0]*n, [0]*m 
        answer = [[0]*m for _ in range(n)]
        parent = [i*m+j for i in range(n) for j in range(m)]
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
            return

        for i in range(n):
            for j in range(m):
                for r, _ in col_seen[matrix[i][j],j]:
                    union(i*m+j,r*m+j)
                for _, c in row_seen[matrix[i][j],i]:
                    union(i*m+j,i*m+c)
                row_seen[matrix[i][j],i].append((i,j))
                col_seen[matrix[i][j],j].append((i,j))
                # for r in range(i+1,n):
                #     if matrix[i][j] == matrix[r][j]:
                #         union(i*m+j,r*m+j)
                # for c in range(j+1,m):
                #     if matrix[i][j] == matrix[i][c]:
                #         union(i*m+j,i*m+c)
        for i in range(n):
            for j in range(m):
                mp[matrix[i][j],find(i*m+j)].append((i,j))

        for k in sorted(mp):
            v = mp[k]
            rank = max(max(answer[i][j],rows[i]+1,cols[j]+1) for i, j in v)
            for i, j in v:
                answer[i][j] = rank 
                rows[i] = rank
                cols[j] = rank 
          
        return answer
