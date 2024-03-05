class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = len(set1 & set2)

        n1 = len(set1)
        n2 = len(set2)
        ans = n1 + n2 - common

        m = len(nums1) // 2
        if n1 > m:
            mn = min(n1 - m, common)
            ans -= n1 - mn - m
            common -= mn

        if n2 > m:
            n2 -= min(n2 - m, common)
            ans -= n2 - m

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/solutions/2594380/tan-xin-pythonjavacgo-by-endlesscheng-ymuh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。