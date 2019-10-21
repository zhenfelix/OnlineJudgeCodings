# import functools

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         @functools.lru_cache(None)
#         def dfs(k,n):
#             # if (k,n) in memo:
#             #     return memo[k,n]
#             if k == 1:
#                 # memo[1,n] = n
#                 return n
#             if n == 0:
#                 # memo[k,1] = 1
#                 return 0
#             # res = float('inf')
#             # for x in range(1,n+1):
#             #     res = min(res, max(dfs(k-1,x-1),dfs(k,n-x))+1)
#             lo, hi = 1, n
#             while lo <= hi:
#                 mid = (lo+hi)//2
#                 if dfs(k,n-mid) > dfs(k-1,mid-1):
#                     lo = mid+1
#                 else:
#                     hi = mid-1
#             if lo == 1 or hi == n:
#                 return 1

#             # return min(max(dfs(k,n-x),dfs(k-1,x-1)) for x in [lo,hi])+1
#             return min(dfs(k,n-hi),dfs(k-1,lo-1))+1
#         return dfs(K,N)
                
        
        
# from collections import defaultdict
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         dp = defaultdict(int)
#         for n in range(N+1):
#             dp[1,n] = n
#         for k in range(2,K+1):
#             dp[k,0], dp[k,1] = 0, 1
#             cut = 1
#             for n in range(2,N+1):
#                 while dp[k,n-(cut+1)] > dp[k-1,(cut+1)-1]:
#                     cut += 1
#                 dp[k,n] = min(dp[k,n-cut],dp[k-1,(cut+1)-1])+1
#         # print(dp)
#         return dp[K,N]

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         dp = [[0]*(N+1) for _ in range(K+1)]
#         for n in range(N+1):
#             dp[1][n] = n
#         for k in range(2,K+1):
#             dp[k][0], dp[k][1] = 0, 1
#             cut = 1
#             for n in range(2,N+1):
#                 while dp[k][n-(cut+1)] > dp[k-1][(cut+1)-1]:
#                     cut += 1
#                 dp[k][n] = min(dp[k][n-cut],dp[k-1][(cut+1)-1])+1
#         # print(dp)
#         return dp[K][N]

# class Solution(object):
#     def superEggDrop(self, K, N):

#         # Right now, dp[i] represents dp(1, i)
#         dp = range(N+1)

#         for k in range(2, K+1):
#             # Now, we will develop dp2[i] = dp(k, i)
#             dp2 = [0]
#             x = 1
#             for n in range(1, N+1):
#                 # Let's find dp2[n] = dp(k, n)
#                 # Increase our optimal x while we can make our answer better.
#                 # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
#                 # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
#                 while x < n and max(dp[x-1], dp2[n-x]) > \
#                                 max(dp[x], dp2[n-x-1]):
#                     x += 1

#                 # The final answer happens at this x.
#                 dp2.append(1 + max(dp[x-1], dp2[n-x]))

#             dp = dp2

#         return dp[-1]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dfs(k,t):
            if (k,t) in memo:
                return memo[k,t]
            if k == 1:
                memo[k,t] = t
                return t
            if t == 1:
                memo[k,t] = 1
                return 1
            memo[k,t] = dfs(k-1,t-1)+dfs(k,t-1)+1
            return memo[k,t]
        memo = {}
        for T in range(1,N+1):
            if dfs(K,T) >= N:
                return T
        return -1



        



# Optimization2: choosing k_1...k_N for each dp[i][1...N]
# To go one step further, till now, we are still finding the optimal floor k from 1 to j for each dp[i][j]. But is this really the smallest range we can narrow? In fact, we can see that the optimal floor k for each dp[i][j] increases as j increases. This means that once we get the optimal k for dp[i][j], we can save current k value and start the next round of for-loop directly, instead of initiating k from 0 again. In this way, in the third for-loop, k will go from 1 to N only once as j in the second for-loop goes from 1 to N. The total time complexity will be O(kn). The code is shown below:




# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         memo = {}
#         for j in range(N+1):
#             memo[1,j] = j
#         for i in range(1,K+1):
#             memo[i,0] = 0
#         def dp(k, n):
#             if (k,n) in memo:
#                 return memo[k,n]
#             ans = math.inf
#             left, right = 1, n
#             while left <= right:
#                 mid = (left+right)//2
                
#                 a, b = dp(k-1,mid-1), dp(k,n-mid)
                
#                 if a < b:
#                     left = mid + 1
#                     ans = min(ans, b)
#                 elif a > b:
#                     right = mid - 1
#                     ans = min(ans, a)
#                 else:
#                     ans = min(ans, a)
#                     break
            
#             # for x in range(1,n+1):
#             #     ans = min(ans, max(dp(k-1,x-1),dp(k,n-x))+1)
#             memo[k,n] = ans+1
#             return ans+1
#         return dp(K,N)



# So I consider this problem in a different way:
# dp[M][K]means that, given K eggs and M moves,
# what is the maximum number of floor that we can check.

# The dp equation is:
# dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         dp = [0]*(K+1)
#         m = 0
#         while dp[K] < N:
#             m += 1
#             tmp = [0]*(K+1)
#             for k in range(1,K+1):
#                 tmp[k] = dp[k-1]+dp[k]+1
#             dp = tmp.copy()
#         return m

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0]*(K+1)
        m = 0
        while dp[-1] < N:
            m += 1
            for k in range(K,0,-1):
                dp[k] += dp[k-1]+1
        return m