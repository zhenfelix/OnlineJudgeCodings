class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        for i, x in enumerate(nums):  # 每个 nums[i] 单独计算 0-1 背包
            if x == 0:
                continue
            f = [True] + [False] * x
            for k, (l, r, val) in enumerate(queries):
                if not l <= i <= r:
                    continue
                for j in range(x, val - 1, -1):
                    f[j] = f[j] or f[j - val]
                if f[x]:  # 满足要求
                    ans = max(ans, k + 1)
                    break
            else:  # 没有中途 break，说明无法满足要求
                return -1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/zero-array-transformation-iv/solutions/3613907/0-1-bei-bao-pythonjavacgo-by-endlesschen-2y0l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。