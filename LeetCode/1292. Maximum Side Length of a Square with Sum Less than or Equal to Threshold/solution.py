# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         res = 0
#         n, m = len(mat), len(mat[0])
#         dp = [[0]*(m+1) for _ in range(n+1)]
#         rows = [[0]*(m+1) for _ in range(n+1)]
#         cols = [[0]*(m+1) for _ in range(n+1)]
#         for i in range(n):
#             for j in range(m)[::-1]:
#                 rows[i][j] = mat[i][j] + rows[i][j+1]
#         for j in range(m):
#             for i in range(n)[::-1]:
#                 cols[i][j] = mat[i][j] + cols[i+1][j]
#         # print(dp)
#         # print(rows)
#         # print(cols)
#         q = collections.deque()
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j] <= threshold:
#                     q.append((i,j,mat[i][j],1))
#         while q:
#             i,j,val,sz = q.popleft()
#             res = max(res,sz)
#             if i-1>=0 and j-1>=0:
#                 val += rows[i-1][j-1]-rows[i-1][j+sz]+cols[i-1][j-1]-cols[i+sz][j-1]-mat[i-1][j-1]
#                 if val <= threshold:
#                     q.append((i-1,j-1,val,sz+1))
#         return res

#         # for sz in range(1,min(n,m)+1):
#         #     # print(dp)
#         #     flag = False
#         #     for i in range(n-sz+1):
#         #         for j in range(m-sz+1):
#         #             dp[i][j] = rows[i][j]-rows[i][j+sz]+cols[i][j]-cols[i+sz][j]-mat[i][j]+dp[i+1][j+1]
#         #             if dp[i][j] <= threshold:
#         #                 flag = True
#         #     if not flag:
#         #         break
#         #     res = sz 
#         # return res



# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         n, m = len(mat), len(mat[0])
#         dp = [[0]*(m+1) for _ in range(n+1)]
#         for i in range(n):
#             for j in range(m):
#                 dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]-dp[i][j]+mat[i][j]
#         for k in range(1,min(n,m)+1)[::-1]:
#             for i in range(n-k+1):
#                 for j in range(m-k+1):
#                     if dp[i+k][j+k]+dp[i][j]-dp[i+k][j]-dp[i][j+k] <= threshold:
#                         return k
#         return 0


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]-dp[i][j]+mat[i][j]

        def valid(k):
            for i in range(n-k+1):
                for j in range(m-k+1):
                    if dp[i+k][j+k]+dp[i][j]-dp[i+k][j]-dp[i][j+k] <= threshold:
                        return True
            return False

        lo, hi = 1, min(n,m)
        while lo <= hi:
            mid = (lo+hi)//2
            if valid(mid):
                lo = mid + 1
            else:
                hi = mid - 1
     
        return hi

