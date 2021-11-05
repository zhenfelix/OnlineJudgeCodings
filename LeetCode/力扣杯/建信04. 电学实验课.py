class Solution:
    def electricityExperiment(self, row: int, col: int, position: List[List[int]]) -> int:
        MOD = 10**9+7
        position = [[c,r] for r, c in position]
        position.sort()
        dp = [1]*row
        mat = [[0]*row for _ in range(row)]
        ones = [[0]*row for _ in range(row)]
        for i in range(row):
            ones[i][i] = 1
            for j in range(-1,2,1):
                if i+j >=0 and i+j < row:
                    mat[i][i+j] = 1
        # print(mat)
        def mul(a, b):
            res = [[0]*row for _ in range(row)]
            for i in range(row):
                for j in range(row):
                    for k in range(row):
                        res[i][j] += a[i][k]*b[k][j]
                        res[i][j] %= MOD
            return res
        def mul_vec(a, x):
            y = [0]*row
            for i in range(row):
                for k in range(row):
                    y[i] += a[i][k]*x[k]
                    y[i] %= MOD
            return y 
        mat_pow = [mat]
        for i in range(31):
            mat_pow.append(mul(mat_pow[-1], mat_pow[-1]))

        def quickmul(x, p):
            for i in range(32):
                if (p>>i)&1:
                    x = mul_vec(mat_pow[i], x)
            return x

        pc = position[0][0]
        for c, r in position:
            dp = quickmul(dp, c-pc)
            for i in range(row):
                if i != r:
                    dp[i] = 0
            pc = c
        return max(dp)