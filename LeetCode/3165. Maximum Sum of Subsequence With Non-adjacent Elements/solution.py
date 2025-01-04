class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # 4 个数分别保存 f00, f01, f10, f11
        t = [[0] * 4 for _ in range(2 << n.bit_length())]

        def maintain(o: int):
            a, b = t[o * 2], t[o * 2 + 1]
            t[o] = [
                max(a[0] + b[2], a[1] + b[0]),
                max(a[0] + b[3], a[1] + b[1]),
                max(a[2] + b[2], a[3] + b[0]),
                max(a[2] + b[3], a[3] + b[1]),
            ]

        # 用 nums 初始化线段树
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                t[o][3] = max(nums[l], 0)
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)

        # 把 nums[i] 改成 val
        def update(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                t[o][3] = max(val, 0)
                return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i, val)
            else:
                update(o * 2 + 1, m + 1, r, i, val)
            maintain(o)

        build(1, 0, n - 1)
        ans = 0
        for i, x in queries:
            update(1, 0, n - 1, i, x)
            ans += t[1][3]  # 注意 f11 没有任何限制，也就是整个数组的打家劫舍
        return ans % 1_000_000_007

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/solutions/2790603/fen-zhi-si-xiang-xian-duan-shu-pythonjav-xnhz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


