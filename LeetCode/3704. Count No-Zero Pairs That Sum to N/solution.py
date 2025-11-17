# 返回两个 1~9 的整数和为 target 的方案数
def two_sum_ways(target: int) -> int:
    return max(min(target - 1, 19 - target), 0)  # 保证结果非负

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)

        # borrowed = True 表示被低位（i+1）借了个 1
        # is_num = True 表示之前填的数位，两个数都无前导零
        @cache
        def dfs(i: int, borrowed: bool, is_num: bool) -> int:
            if i < 0:
                # borrowed 必须为 False
                return 0 if borrowed else 1

            d = s[i] - borrowed
            res = 0

            # 情况一：两个数位都不为 0
            if is_num:
                res = dfs(i - 1, False, True) * two_sum_ways(d)  # 不向高位借 1
                res += dfs(i - 1, True, True) * two_sum_ways(d + 10) # 向高位借 1

            # 情况二：其中一个数位填前导零
            if i < m - 1:  # 不能是最低位
                if d:
                    # 如果 d < 0，必须向高位借 1
                    # 如果 is_num = True，根据对称性，方案数要乘以 2
                    res += dfs(i - 1, d < 0, False) * (is_num + 1)
                elif i == 0:  # 两个数位都填 0，只有当 i = 0 的时候才有解
                    res += 1

            return res

        return dfs(m - 1, False, True)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-no-zero-pairs-that-sum-to-n/solutions/3798539/cong-di-wang-gao-de-shu-wei-dppythonjava-r8dh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。