class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for x in range(100):
            s = str(x)
            if all(str(a) not in s for a in nums1):
                continue
            if all(str(a) not in s for a in nums2):
                continue
            return x
        return -1

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        s = s1 & s2
        if s: return min(s)
        x, y = min(nums1), min(nums2)
        return min(x * 10 + y, y * 10 + x)


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/3Cqiwp/view/uIYhPw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。