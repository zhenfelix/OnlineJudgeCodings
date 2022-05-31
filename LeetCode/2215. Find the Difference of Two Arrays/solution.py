class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        ans = [set(),set()]
        for x in nums1:
            if x not in s2:
                ans[0].add(x)
        for x in nums2:
            if x not in s1:
                ans[-1].add(x)
        return [list(ans[0]),list(ans[-1])]


class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]