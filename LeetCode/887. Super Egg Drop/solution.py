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