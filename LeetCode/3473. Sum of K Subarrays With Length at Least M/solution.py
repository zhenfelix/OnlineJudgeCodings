class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))  # 前缀和
        f = [0] * (n + 1)
        for i in range(1, k + 1):
            nf = [-inf] * (n + 1)
            mx = -inf
            # 左右两边留出足够空间给其他子数组
            for j in range(i * m, n - (k - i) * m + 1):
                # mx 表示最大的 f[L]-s[L]，其中 L 在区间 [(i-1)*m, j-m] 中
                mx = max(mx, f[j - m] - s[j - m])
                nf[j] = max(nf[j - 1], mx + s[j])  # 不选 vs 选
            f = nf
        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-k-subarrays-with-length-at-least-m/solutions/3591733/hua-fen-xing-dp-qian-zhui-he-shi-zi-bian-3k0w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。