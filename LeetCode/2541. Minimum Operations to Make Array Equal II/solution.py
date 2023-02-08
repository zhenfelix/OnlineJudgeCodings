class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 != nums2:
                return -1
            return 0
        pos = neg = 0
        n = len(nums1)
        for i in range(n):
            delta = nums1[i]-nums2[i]
            if delta%k:
                return -1
            if delta >= 0:
                pos += (delta//k)
            else:
                neg += ((-delta)//k)
        if pos != neg:
            return -1
        return pos