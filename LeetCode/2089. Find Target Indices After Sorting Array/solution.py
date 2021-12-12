class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_right(nums, target)
        if lo < hi:
            return [i for i in range(lo,hi)]
        return []