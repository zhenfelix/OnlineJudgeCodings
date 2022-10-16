class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = 0, 0
        na, nb = len(nums1), len(nums2)
        if nb&1:
            for x in nums1:
                a ^= x  
        if na&1:
            for y in nums2:
                b ^= y  
        return a^b

# class Solution:
#     def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
#         a, b = 0, 0
#         na, nb = len(nums1), len(nums2)
#         for x in nums1:
#             a ^= x  
#         if nb%2 == 0:
#             a = 0
#         for y in nums2:
#             b ^= y  
#         if na%2 == 0:
#             b = 0
#         return a^b