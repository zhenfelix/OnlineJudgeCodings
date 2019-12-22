# class Solution:
#     def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
#         n, m = len(grid), len(grid[0])
#         parent = [-1]*(n*m)
#         cc = collections.defaultdict(int)
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     parent[i*m+j] = i*m+j
#                     cc[i*m+j] = 1
#         for i, j in hits:
#             parent[i*m+j] = -1
#             cc[i*m+j] = 0

#         def find(cur):
#             if cur == parent[cur]:
#                 return cur
#             root = find(parent[cur])
#             parent[cur] = root
#             return root

#         def union(a, b):
#             ra, rb = find(a), find(b)
#             cnt = 0
#             if ra == rb:
#                 return 0
#             if ra > rb:
#                 ra, rb = rb, ra 
#             if rb >= m and ra < m:
#                 cnt = cc[rb]
#             parent[rb] = ra 
#             cc[ra] += cc[rb]
#             cc[rb] = 0
#             return cnt

#         def connect(center):
#             cnt = 0
#             x, y = center//m, center%m
#             for row, col in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
#                 if 0 <= row < n and 0 <= col < m and parent[row*m+col] != -1:
#                     cnt += union(center,row*m+col)
#             return cnt

#         for i in range(n):
#             for j in range(m):
#                 if parent[i*m+j] != -1:
#                     connect(i*m+j)

#         res = []
#         for i, j in hits[::-1]:
#             if grid[i][j] != 0:
#                 parent[i*m+j] = i*m+j
#                 tmp = connect(i*m+j)
#                 cc[find(i*m+j)] += 1
#                 # if tmp > 0 and i*m+j >= m:
#                 #     tmp -= 1
#                 res.append(tmp)
#             else:
#                 res.append(0)
#         return res[::-1]




class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])
        
        # Connect unconnected bricks and 
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j]!=1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += sum(dfs(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            return ret
        
        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
                
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j]==1 and is_connected(i, j):
                ret[k] = dfs(i, j)-1
            
        return ret