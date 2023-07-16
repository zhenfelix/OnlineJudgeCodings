class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = [1]*n 
        dp2 = [1]*n 
        ans = 1
        for i in range(1,n):
            if nums1[i] >= nums1[i-1]:
                dp1[i] = max(dp1[i],dp1[i-1]+1)
            if nums1[i] >= nums2[i-1]:
                dp1[i] = max(dp1[i],dp2[i-1]+1)
            if nums2[i] >= nums2[i-1]:
                dp2[i] = max(dp2[i],dp2[i-1]+1)
            if nums2[i] >= nums1[i-1]:
                dp2[i] = max(dp2[i],dp1[i-1]+1)
            ans = max(ans,dp1[i],dp2[i])
        return ans 


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums = (nums1, nums2)
        f = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            for j in range(2):
                if nums1[i - 1] <= nums[j][i]:
                    f[i][j] = f[i - 1][0] + 1
                if nums2[i - 1] <= nums[j][i]:
                    f[i][j] = max(f[i][j], f[i - 1][1] + 1)
        return max(map(max, f))


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/mmSJFF/view/7GU7bm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans = f0 = f1 = 1
        for (x0, y0), (x1, y1) in pairwise(zip(nums1, nums2)):
            f = g = 1
            if x0 <= x1: f = f0 + 1
            if y0 <= x1: f = max(f, f1 + 1)
            if x0 <= y1: g = f0 + 1
            if y0 <= y1: g = max(g, f1 + 1)
            f0, f1 = f, g
            ans = max(ans, f0, f1)
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/mmSJFF/view/7GU7bm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。