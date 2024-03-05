from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        sum_left = sum(nums[:dist + 2])
        L = SortedList(nums[1:dist + 2])
        R = SortedList()

        def L2R() -> None:
            x = L.pop()
            nonlocal sum_left
            sum_left -= x
            R.add(x)

        def R2L() -> None:
            x = R.pop(0)
            nonlocal sum_left
            sum_left += x
            L.add(x)

        while len(L) > k:
            L2R()

        ans = sum_left
        for i in range(dist + 2, len(nums)):
            # 移除 out
            out = nums[i - dist - 1]
            if out in L:
                sum_left -= out
                L.remove(out)
            else:
                R.remove(out)

            # 添加 in
            in_val = nums[i]
            if in_val < L[-1]:
                sum_left += in_val
                L.add(in_val)
            else:
                R.add(in_val)

            # 维护大小
            if len(L) == k - 1:
                R2L()
            elif len(L) == k + 1:
                L2R()

            ans = min(ans, sum_left)

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/solutions/2614067/liang-ge-you-xu-ji-he-wei-hu-qian-k-1-xi-zdzx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。