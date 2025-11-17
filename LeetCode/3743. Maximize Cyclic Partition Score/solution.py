# 手写 max 更快
fmax = lambda a, b: b if b > a else a

class Solution:
    # 3573. 买卖股票的最佳时机 V
    def maximumProfit(self, prices: List[int], k: int) -> int:
        f = [[-inf] * 3 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for p in prices:
            for j in range(k + 1, 0, -1):
                f[j][0] = fmax(f[j][0], fmax(f[j][1] + p, f[j][2] - p))
                f[j][1] = fmax(f[j][1], f[j - 1][0] - p)
                f[j][2] = fmax(f[j][2], f[j - 1][0] + p)
        return f[-1][0]

    def maximumScore(self, nums: List[int], k: int) -> int:
        max_i = nums.index(max(nums))
        ans1 = self.maximumProfit(nums[max_i:] + nums[:max_i], k)  # nums[max_i] 是第一个数
        ans2 = self.maximumProfit(nums[max_i + 1:] + nums[:max_i + 1], k)  # nums[max_i] 是最后一个数
        return fmax(ans1, ans2)

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximize-cyclic-partition-score/solutions/3827101/zhao-dao-zui-jia-duan-huan-wei-zhi-zhuan-k2ip/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。