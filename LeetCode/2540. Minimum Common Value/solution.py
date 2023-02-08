class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        j = 0
        for i in range(n):
            while j < m and nums2[j] <= nums1[i]:
                if nums1[i] == nums2[j]:
                    return nums1[i]
                j += 1  
        return -1