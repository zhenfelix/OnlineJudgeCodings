class Solution:
    def maxSum(self, A, B):
        i, j, n, m = 0, 0, len(A), len(B)
        a, b, res, mod = 0, 0, 0, 10**9 + 7
        while i < n or j < m:
            if i < n and (j == m or A[i] < B[j]):
                a += A[i]
                i += 1
            elif j < m and (i == n or A[i] > B[j]):
                b += B[j]
                j += 1
            else:
                res += max(a, b) + A[i]
                i += 1
                j += 1
                a, b = 0, 0
        return (res + max(a, b)) % mod        


# class Solution:
#     def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
#         n1, n2 = len(nums1), len(nums2)
#         arr1, arr2 = [0], [0]
#         i, j = 0, 0
#         cnt1, cnt2 = 0, 0
#         while i < n1 or j < n2:
#             if i == n1:
#                 arr2[-1] += nums2[j]
#                 j += 1
#             elif j == n2:
#                 arr1[-1] += nums1[i]
#                 i += 1
#             elif nums1[i] < nums2[j]:
#                 arr1[-1] += nums1[i]
#                 i += 1
#             elif nums1[i] > nums2[j]:
#                 arr2[-1] += nums2[j]
#                 j += 1
#             else:
#                 arr1[-1] += nums1[i]
#                 arr2[-1] += nums2[j]
#                 arr1.append(0)
#                 arr2.append(0)
#                 i += 1
#                 j += 1
#         res = 0
#         for i in range(len(arr1)):
#             res += max(arr1[i],arr2[i])
#         return res%(10**9+7)