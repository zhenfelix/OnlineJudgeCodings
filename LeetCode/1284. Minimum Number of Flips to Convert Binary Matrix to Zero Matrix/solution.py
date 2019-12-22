# class Solution:
#     def minFlips(self, mat: List[List[int]]) -> int:
#         n, m = len(mat), len(mat[0])
#         cur = 0
#         for i in range(n):
#             for j in range(m):
#                 cur += (mat[i][j]<<(i*m+j))
#         q = collections.deque()
#         visited = set()
#         q.append(cur)
#         visited.add(cur)
#         level = 0
#         while q:
#             sz = len(q)
#             for _ in range(sz):
#                 cur = q.popleft()
#                 # print(cur,level)
#                 if cur == 0:
#                     return level
#                 for i in range(n):
#                     for j in range(m):
#                         nxt = cur
#                         positions = [i*m+j]
#                         for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                             ii = i + dx
#                             jj = j + dy
#                             if 0 <= ii < n and 0 <= jj < m:
#                                 positions.append(ii*m+jj)
#                         for pos in positions:
#                             if 0 <= pos < n*m:
#                                 nxt ^= (1<<pos)
#                         # print(i,j,positions)
#                         # print(nxt)
#                         if nxt not in visited:
#                             visited.add(nxt)
#                             q.append(nxt)
#             level += 1
#         return -1

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << i * n + j for i, row in enumerate(mat) for j, cell in enumerate(row))
        dq = collections.deque([(start, 0)])
        seen = set([start])
        while dq:
            cur, step = dq.popleft()
            if not cur:
                return step
            for i in range(m):
                for j in range(n):
                    next = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if r >= 0 and r < m and c >= 0 and c < n:
                            next ^= 1 << r * n + c
                    if next not in seen:
                        seen.add(next)
                        dq.append((next, step + 1))
        return -1