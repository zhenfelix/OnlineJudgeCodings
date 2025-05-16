class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        if sum(nums) < abs(k):  # |k| 太大
            return -1

        n = len(nums)
        ans = -1

        @cache  # 当 vis 哈希表用
        def dfs(i: int, s: int, m: int, odd: bool, empty: bool) -> None:
            nonlocal ans
            if ans == limit or m > limit and ans >= 0:  # 无法让 ans 变得更大
                return

            if i == n:
                if not empty and s == k and m <= limit:  # 合法子序列
                    ans = max(ans, m)  # 用合法子序列的元素积更新答案的最大值
                return

            # 不选 x
            dfs(i + 1, s, m, odd, empty)

            # 选 x
            x = nums[i]
            dfs(i + 1, s + (-x if odd else x), min(m * x, limit + 1), not odd, False)

        dfs(0, 0, 1, False, True)
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/solutions/3641716/bao-li-sou-suo-by-endlesscheng-j3bl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。