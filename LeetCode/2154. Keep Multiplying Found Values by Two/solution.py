class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for x in sorted(nums):
            if x > original:
                break
            if x == original:
                original *= 2
        return original


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/UECpIR/view/6QKQ4h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        p = original
        multiples = defaultdict(int)
        while p <= 1000:
            multiples[p] = 1
            p *= 2
        for x in nums:
            if multiples[x] == 1:
                multiples[x] = 2
        while multiples[original] == 2:
            original *= 2
        return original


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask = 0
        for x in nums:
            if x%original == 0:
                p = x//original
                if p&(p-1) == 0:
                    mask |= p
        mask = ~mask
        return original*(mask&(-mask))
