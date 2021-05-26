class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        i = j = 0
        res = 0
        while i < n:
            while j < m and nums2[j] >= nums1[i]:
                j += 1
            res = max(res, max(0,j-i-1))
            i += 1
        return res