class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9+7
        mat = [[1]*7 for _ in range(7)]
        for i in range(1,7):
            for j in range(1,7):
                mat[i][j] = math.gcd(i,j)
        # print("mat: ", mat)
        dp = [[0]*7 for _ in range(7)]
        for i in range(1,7):
            dp[i][0] = 1
        for _ in range(n-1):
            ndp = [[0]*7 for _ in range(7)]
            for cur in range(1,7):
                for i in range(1,7):
                    for j in range(7):
                        if mat[cur][i] == 1 and cur not in [i,j]:
                            ndp[cur][i] += dp[i][j]
            dp = ndp
            # print(dp)
        ans = 0
        for aa in dp:
            for a in aa:
                ans += a 
        return ans%MOD
                         

class Solution:
    def distinctSequences(self, n: int) -> int:
        @cache
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        @cache
        def getRes(idx, last_two):
            # 当前位置是idx，前面状态是last_two
            if idx == n: return 1
            queue = last_two
            ans = 0
            for i in range(1, 7):
                if i != queue[0] and i != queue[1] and (gcd(i, queue[1]) == 1 or queue[1] == 0):
                    ans += getRes(idx+1, (queue[1], i))
                    ans %= 10 ** 9 + 7
            return ans
        return getRes(0, (0, 0))



MOD, MX = 10 ** 9 + 7, 10 ** 4
f = [[[0] * 6 for _ in range(6)] for _ in range(MX + 1)]
f[2] = [[int(j != i and gcd(j + 1, i + 1) == 1) for j in range(6)] for i in range(6)]
for i in range(2, MX):
    for j in range(6):
        for last in range(6):
            if last != j and gcd(last + 1, j + 1) == 1:
                f[i + 1][j][last] = sum(f[i][last][last2] for last2 in range(6) if last2 != j) % MOD

class Solution:
    def distinctSequences(self, n: int) -> int:
        return sum(sum(row) for row in f[n]) % MOD if n > 1 else 6


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/number-of-distinct-roll-sequences/solution/by-endlesscheng-tgkn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




import numpy as np
Mod = np.uint64(10**9 + 7)
def matpow_mod(mat, b):
    n = len(mat)
    ret = np.eye(n, n, dtype=np.uint64) 
    while b:
        if b&1:
            ret = (ret@mat)%Mod
        b >>= 1
        mat = (mat@mat)%Mod
    return ret

maxpt = 6
n_sta = maxpt*maxpt
mat = np.zeros((n_sta, n_sta), np.uint64)
for lv3, lv2, lv1 in permutations(range(1, maxpt+1), 3):
    if gcd(lv3, lv2) == 1 and gcd(lv2, lv1)==1:        
        mat[(lv2-1)*maxpt + (lv1-1)][(lv3-1)*maxpt +(lv2-1)] = 1    
    
    

# 方便起见, 不合法状态初始值也设为1, 因此n<=2的时候要特判
inidp = np.ones((n_sta, ), np.uint64)

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6
        if n == 2: return 22
        
        dp = matpow_mod(mat, n-2)@inidp
        return int(sum(dp)%Mod)


# 作者：migeater
# 链接：https://leetcode.cn/problems/number-of-distinct-roll-sequences/solution/ju-zhen-by-migeater-9ow0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


