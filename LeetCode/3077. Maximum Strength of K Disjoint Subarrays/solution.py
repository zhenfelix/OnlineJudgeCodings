class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        dp0 = [-inf] * (k + 1)
        dp1 = [-inf] * (k + 1)
        dp0[0] = dp1[0] = 0
        for num in nums:
            # dp0 表示最后一个元素在第 i 个数组中的状态
            # 两种转移过来：前一个位置是否截断
            # dp1 表示该位置第 i 个数组已经截断的情况下的最大价值
            for i in range(k, 0, -1):
                dp0[i] = max(dp0[i], dp1[i-1])
                dp0[i] += (1 if i % 2 else -1) * num * (k - i + 1)
                dp1[i] = max(dp1[i], dp0[i])
        return dp1[-1]

# 作者：小羊肖恩
# 链接：https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays/solutions/2678091/xiao-yang-xiao-en-xian-duan-shang-de-zhu-ea5g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。