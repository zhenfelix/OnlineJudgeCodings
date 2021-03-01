# class Solution:
#     def init(self):
#         total, choice = 10**4+15, 15
#         self.dp = [[0]*choice for _ in range(total)]
#         for i in range(total):
#             self.dp[i][0] = 1
#         for i in range(1,total):
#             for j in range(1,min(i+1,choice)):
#                 self.dp[i][j] = self.dp[i-1][j] + self.dp[i-1][j-1]
#                 self.dp[i][j] %= self.MOD

#     def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
#         res, self.MOD = [], 10**9+7
#         self.init()
#         # print(self.dp)
#         for n, k in queries:
#             # print(n,k)
#             f, mul, cur = 2, 1, k
#             while f*f <= k and f <= cur:
#                 if cur%f == 0:
#                     cnt = 0
#                     while cur%f == 0:
#                         cnt += 1
#                         cur //= f 
#                     mul *= self.dp[n+cnt-1][cnt]
#                     mul %= self.MOD
#                     # print(f,cnt,mul,cur)
#                 f += 1
#             if cur > 1:
#                 mul *= self.dp[n][1]
#                 mul %= self.MOD
#             res.append(mul)
#         return res 

class Solution:
    is_inited = False
    MOD = 10**9+7
    # total, choice = 10**4+15, 15
    # dp = [[0]*15 for _ in range(10**4+15)]


    def init(self):
        if Solution.is_inited:
            return
        total, choice = 10**4+15, 15
        Solution.dp = [[0]*choice for _ in range(total)]
        Solution.is_inited = True
        for i in range(total):
            Solution.dp[i][0] = 1
        for i in range(1,total):
            for j in range(1,min(i+1,choice)):
                Solution.dp[i][j] = Solution.dp[i-1][j] + Solution.dp[i-1][j-1]
                Solution.dp[i][j] %= Solution.MOD

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        res = []
        self.init()
        # print(self.dp)
        for n, k in queries:
            # print(n,k)
            f, mul, cur = 2, 1, k
            while f*f <= k and f <= cur:
                if cur%f == 0:
                    cnt = 0
                    while cur%f == 0:
                        cnt += 1
                        cur //= f 
                    mul *= Solution.dp[n+cnt-1][cnt]
                    mul %= Solution.MOD
                    # print(f,cnt,mul,cur)
                f += 1
            if cur > 1:
                mul *= Solution.dp[n][1]
                mul %= Solution.MOD
            res.append(mul)
        return res 

