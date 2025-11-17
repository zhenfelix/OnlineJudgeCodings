# 更快的写法见【Python3 写法二】
class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        f = [[0, 0], [0, 0]]
        for x in nums:
            x %= 2
            f[x][1] = (f[x][1] + f[x][0]) % MOD
            f[x][0] = (f[x][0] + f[x ^ 1][0] + f[x ^ 1][1] + 1) % MOD
        return (f[0][0] + f[0][1] + f[1][0] + f[1][1]) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-stable-subsequences/solutions/3781347/he-fa-zi-xu-lie-dppythonjavacgo-by-endle-7sz0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。