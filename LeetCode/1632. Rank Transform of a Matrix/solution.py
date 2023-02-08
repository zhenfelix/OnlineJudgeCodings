class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        tot = n*m 
        parent = list(range(tot))
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv 
            return 
        for i in range(n):
            mp = dict()
            for j in range(m):
                v = matrix[i][j]
                if v in mp:
                    k = mp[v]
                    connect(i*m+j,i*m+k)
                mp[v] = j 
        for j in range(m):
            mp = dict()
            for i in range(n):
                v = matrix[i][j]
                if v in mp:
                    k = mp[v]
                    connect(i*m+j,k*m+j)
                mp[v] = i
        arr = []
        for i in range(n):
            for j in range(m):
                v = matrix[i][j]
                g = find(i*m+j)
                arr.append((v,g,i,j))
        arr.sort()
        row = [0]*n 
        col = [0]*m 
        rank = [[0]*m for _ in range(n)]
        right = 0
        for left in range(tot):
            if left < right: continue
            mx = 0
            while right < tot and arr[left][1] == arr[right][1]:
                v, g, i, j = arr[right]
                mx = max(mx, row[i])
                mx = max(mx, col[j])
                right += 1
            mx += 1
            for z in range(left,right):
                v, g, i, j = arr[z]
                rank[i][j] = mx 
                row[i] = col[j] = mx
        return rank

class Solution: 

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]: 

        LIM = 512

        R, C = len(matrix), len(matrix[0])

        res = [[0]*C for _ in range(R)]

        countR, countC = [0]*R, [0]*C

        

        # 按元素大小分别存储元素坐标

        ls = collections.defaultdict(list)

        for r, row in enumerate(matrix): 

            for c, val in enumerate(row): 

                ls[val].append((r, c))

                

        # 并查集用于合并行或列相同的元素

        union = list(range(LIM*2))

        def find(i): 

            if union[i] == i: return i

            union[i] = find(union[i])

            return union[i]

        

        # 按val从小到大遍历

        pool = collections.defaultdict(list)

        for val in sorted(ls.keys()): 



            # 用并查集合并行和列相同的元素并分组

            for r, c in ls[val]: 

                union[find(r)] = find(c+LIM)

            pool.clear()

            for r, c in ls[val]: 

                pool[find(r)].append((r, c))



                

            # 行和列相同的元素，共享相同的rank

            for group in pool.values(): 

                rank = max(max((countR[r], countC[c])) for r, c in group) + 1

                for r, c in group: 

                    countR[r] = countC[c] = res[r][c] = rank

                    # 重置并查集

                    union[r] = r

                    union[c+LIM] = c+LIM

        return res

作者：Simpleson
链接：https://leetcode.cn/problems/rank-transform-of-a-matrix/solutions/459805/python3-mei-sha-ji-zhu-han-liang-de-ti-jie-by-simp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
