MOD = 10**9+7
N, M = 10000+20, 20
cb = [[0]*M for _ in range(N)]
for i in range(N):
    cb[i][0] = 1
    for j in range(1,min(i+1,M)):
        cb[i][j] = (cb[i-1][j]+cb[i-1][j-1])%MOD

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ans = []
        for n, k in queries:
            n -= 1
            cur, f = 1, 2
            while f*f <= k:
                cnt = 0
                while k%f == 0:
                    cnt += 1
                    k //= f 
                cur = (cur*cb[n+cnt][cnt])%MOD
                # print(f,k,cnt,cb[n+cnt][cnt])
                f += 1
            if k > 1:
                cur = (cur*cb[n+1][1])%MOD
            ans.append(cur)
        return ans


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

