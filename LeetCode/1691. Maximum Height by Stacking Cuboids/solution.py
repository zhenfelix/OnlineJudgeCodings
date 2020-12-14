class Solution:
    def maxHeight(self, A):
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        for j in range(1, len(A)):
            for i in range(j):
                # 充分必要条件！
                if all(A[i][k] <= A[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)        



from functools import lru_cache
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids.append([0,0,0])
        cuboids.sort(key=lambda x: x[0]*x[1]*x[2])
        n = len(cuboids)
        dp = [[0]*3 for _ in range(n)]
        res = 0
        for i in range(1,n):
            for pi in range(3):
                cur = [cuboids[i][k] for k in range(3) if k != pi]
                for j in range(i):
                    for pj in range(3):
                        if cuboids[j][pj] > cuboids[i][pi]:
                            continue
                        pre = [cuboids[j][k] for k in range(3) if k != pj]
                        if all(pre[i] <= cur[i] for i in range(2)) or all(pre[i] <= cur[1-i] for i in range(2)):
                            dp[i][pi] = max(dp[i][pi], cuboids[i][pi]+dp[j][pj])
                            res = max(res, dp[i][pi])

        # def dfs(idx,pos):
        #     res = 0
        #     cur = [cuboids[idx][k] for k in range(3) if k != pos]
        #     for j in range(idx):
        #         for p in range(3):
        #             pre = [cuboids[j][k] for k in range(3) if k != p]
        #             if all(pre[i] <= cur[i] for i in range(2)) or all(pre[i] <= cur[1-i] for i in range(2)):
        #                 res = max(res, cuboids[idx][pos]+dfs(j,p))
        # print(cuboids)
        # print(dp)
        # print(max(dp))
        return res