class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        left = Counter([x+y for x in nums1 for y in nums2])
        right = Counter([x+y for x in nums3 for y in nums4])
        res = 0
        for k, v in left.items():
            res += v*right[-k]
        return res