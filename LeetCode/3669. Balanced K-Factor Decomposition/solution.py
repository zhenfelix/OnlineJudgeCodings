# 预处理每个数的因子
MX = 100_001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        min_diff = inf
        path = [0] * k
        ans = None

        def dfs(i: int, n: int, mn: int, mx: int) -> None:
            if i == k - 1:
                nonlocal min_diff, ans
                d = max(mx, n) - min(mn, n)  # 最后一个数是 n
                if d < min_diff:
                    min_diff = d
                    path[i] = n
                    ans = path.copy()  # path[:]
                return
            for d in divisors[n]:  # 枚举 x 的因子
                path[i] = d  # 直接覆盖，无需恢复现场
                dfs(i + 1, n // d, min(mn, d), max(mx, d))

        dfs(0, n, inf, 0)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/balanced-k-factor-decomposition/solutions/3768233/bao-sou-pythonjavacgo-by-endlesscheng-x7jt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。