class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 1
            ans = float('inf')
            if arr[i] == arr[j]:
                ans = dfs(i+1,j-1)
            for k in range(i,j):
                ans = min(ans, dfs(i,k)+dfs(k+1,j))
            return ans
        n = len(arr)
        return dfs(0,n-1)



class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for sz in range(n):
            if sz == 0:
                for i in range(n):
                    dp[i][i] = 1
            else:
                for i in range(n-sz):
                    j = i + sz
                    dp[i][j] = dp[i+1][j] + 1
                    if arr[i] == arr[i+1]:
                        dp[i][j] = min(dp[i][j], 1+dp[i+2][j])
                    for k in range(i+2,j+1):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1]+dp[k+1][j])
        return dp[0][n-1]







# class Solution:
#     def minimumMoves(self, arr: List[int]) -> int:
#         n = len(arr)
#         dp = collections.defaultdict(int)
#         for i in range(n):
#             dp[i,i] = 1
#         for i in range(1,n):
#             dp[i-1,i] = (1 if arr[i-1] == arr[i] else 2)
#         for sz in range(3,n+1):
#             left = 0
#             while left+sz-1 < n:
#                 right = left+sz-1
#                 dp[left,right] = sz
#                 if arr[left] == arr[right]:
#                     dp[left,right] = min(dp[left,right], dp[left+1,right-1])
#                 for k in range(left,right):
#                     dp[left,right] = min(dp[left,right],dp[left,k]+dp[k+1,right])
#                 left += 1
#         return dp[0,n-1]


# class Solution:
#     def minimumMoves(self, arr: List[int]) -> int:
#         n = len(arr)
#         dp = [[n]*n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 1
#         for i in range(1,n):
#             dp[i-1][i] = (1 if arr[i-1] == arr[i] else 2)
#         for sz in range(3,n+1):
#             left = 0
#             while left+sz-1 < n:
#                 right = left+sz-1
#                 if arr[left] == arr[right]:
#                     dp[left][right] = min(dp[left][right], dp[left+1][right-1])
#                 for k in range(left,right):
#                     dp[left][right] = min(dp[left][right],dp[left][k]+dp[k+1][right])
#                 left += 1
#         return dp[0][n-1]


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[n]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1,n):
            dp[i-1][i] = (1 if arr[i-1] == arr[i] else 2)
        for sz in range(3,n+1):
            left = 0
            for left in range(n-sz+1):
                right = left+sz-1
                if arr[left] == arr[right]:
                    dp[left][right] = min(dp[left][right], dp[left+1][right-1])
                # for k in range(left,right):
                #     dp[left][right] = min(dp[left][right],dp[left][k]+dp[k+1][right])
                else:
                    dp[left][right] = min([dp[left][k]+dp[k+1][right] for k in range(left,right)])
        return dp[0][n-1]


# class Solution(object):
#     def minimumMoves(self, A):
#         dp = [[len(A) for i in A] for j in A]
#         for i in range(len(A)):
#             dp[i][i] = 1
#         for i in range(len(A)-1):
#             dp[i][i+1] = 1 if A[i] == A[i+1] else 2
#         for size in range(3,len(A)+1):
#             for l in range(len(A)-size+1):
#                 r = l+size-1
#                 if A[l] == A[r]:
#                     dp[l][r] = dp[l+1][r-1]
#                 else:
#                     dp[l][r] = min([dp[l][mid]+dp[mid+1][r] for mid in range(l,l+size-1)])
#         return dp[0][len(A)-1]