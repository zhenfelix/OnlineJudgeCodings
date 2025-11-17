class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, g: int) -> int:
            if i < 0:
                return 1 if g == 1 else 0
            return sum(dfs(i - 1, gcd(g, x)) for x in mat[i]) % MOD

        return dfs(len(mat) - 1, 0)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-ways-to-choose-coprime-integers-from-rows/solutions/3815551/liang-chong-fang-fa-dong-tai-gui-hua-bei-4djl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        mx = 0 
        for i in range(n):
            for j in range(m):
                mx = max(mx,mat[i][j])
        MOD = 10**9+7
        dp = [0]*(mx+1)
        dp[0] = 1

        for row in mat:
            ndp = [0]*(mx+1)
            for x in row:
                for y in range(mx+1):
                    g = gcd(x,y)
                    ndp[g] += dp[y]
                    ndp[g] %= MOD
            dp = ndp
        return dp[1]
