class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(m: int) -> bool:
            cnt = 0
            for i in range(1, 1 << len(coins)):  # 枚举所有非空子集
                lcm_res = 1  # 计算子集 LCM
                for j, x in enumerate(coins):
                    if i >> j & 1:
                        lcm_res = lcm(lcm_res, x)
                        if lcm_res > m:  # 太大了
                            break
                else:  # 中途没有 break
                    cnt += m // lcm_res if i.bit_count() % 2 else -(m // lcm_res)
            return cnt >= k
        return bisect_left(range(min(coins) * k), True, k, key=check)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/solutions/2739205/er-fen-da-an-rong-chi-yuan-li-pythonjava-v24i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。