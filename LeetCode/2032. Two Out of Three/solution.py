# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         nums1 = set(nums1)
#         nums2 = set(nums2)
#         nums3 = set(nums3)
#         cc = Counter()
#         for x in nums1:
#             cc[x] += 1
#         for x in nums2:
#             cc[x] += 1
#         for x in nums3:
#             cc[x] += 1
#         res = []
#         for k, v in cc.items():
#             if v >= 2:
#                 res.append(k)
#         return res

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        return list((s1 & s2) | (s1 & s3) | (s2 & s3))


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/2ELXyY/view/DxDKIC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。