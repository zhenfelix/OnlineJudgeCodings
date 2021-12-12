class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mi, mx = min(nums), max(nums)
        lo, hi = -1, -1
        for i, x in enumerate(nums):
            if x == mi:
                lo = i 
            if x == mx:
                hi = i 
        if lo > hi:
            lo, hi = hi, lo
        return min(hi+1,n-lo,lo+1+n-hi)


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        l = nums.index(min(nums))
        r = nums.index(max(nums))
        if l > r:
            l, r = r, l
        return min(n - (r - l - 1), r + 1, n - l)


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。