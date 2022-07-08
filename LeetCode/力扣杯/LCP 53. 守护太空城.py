# class Solution:
#     def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
#         mask = defaultdict(int)
#         P, T = 0, 0
#         for p, t in zip(position, time):
#             mask[p] |= (1<<(t-1))
#             P = max(P, p)
#             T = max(T, t)

#         double = [0]*(1<<T)
#         single = [0]*(1<<T)
#         for s in range(1,1<<T):
#             pre = 0
#             for i in range(T):
#                 cur = (s>>i)&1
#                 if pre == 0:
#                     single[s] += 2*cur
#                     double[s] += 3*cur
#                 else:
#                     single[s] += cur
#                     double[s] += cur
#                 pre = cur

#         dp = [float('inf')]*(1<<T)
#         dp[0] = 0
#         tot = (1<<T)
#         for p in range(P+1):
#             ndp = [float('inf')]*tot
#             for cur in range(tot):
#                 s = (tot-1)^cur
#                 pre = s 
#                 while True:
#                     ndp[cur] = min(ndp[cur], dp[pre]+double[cur]+single[(s^pre)&mask[p]])
#                     if pre == 0:
#                         break
#                     pre = (pre-1)&s
#             dp = ndp
#             # print(p, dp)
#         # return min(dp)
#         return dp[0]

class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
        n, m = max(position), 1 << max(time)
        rain = [0] * (n + 1)
        for t, p in zip(time, position):
            rain[p] |= 1 << (t - 1)

        union = [0] * m
        single = [0] * m
        for i in range(1, m):
            lb = i & -i
            j = i ^ lb
            lb2 = j & -j
            union[i] = union[j] + (1 if lb == (lb2 >> 1) else 3)  # lb == (lb2 >> 1) 表示两个时间点相邻
            single[i] = single[j] + (1 if lb == (lb2 >> 1) else 2)  # 递推

        f = [[inf] * m for _ in range(n + 1)]
        for j in range(m):
            f[0][j] = union[j] + single[((m - 1) ^ j) & rain[0]]
        for i in range(1, n + 1):
            for j in range(m):
                pre = mask = (m - 1) ^ j
                while True:  # 枚举 j 的补集 mask 中的子集 pre
                    cost = f[i - 1][pre] + union[j] + single[(mask ^ pre) & rain[i]]
                    f[i][j] = min(f[i][j], cost)
                    if pre == 0:
                        break
                    pre = (pre - 1) & mask
        return f[n][0]


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/EJvmW4/solution/by-endlesscheng-pk2q/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。