class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(A, B):
            cc = Counter(A)
            res = 0
            for b in B:
                t = b*b 
                for k, v in cc.items():
                    if t%k != 0:
                        continue
                    elif t == k*k:
                        res += cc[k]*(cc[k]-1)
                    else:
                        res += cc[k]*cc[t//k]
            return res//2
        return count(nums1,nums2) + count(nums2,nums1)


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(arr1, arr2):
            cc = Counter()
            res = 0
            for i, x in enumerate(arr1):
                cc[x*x] += 1
            n = len(arr2)
            for j in range(n):
                for k in range(j+1, n):
                    res += cc[arr2[j]*arr2[k]]
            return res

        return helper(nums1,nums2) + helper(nums2,nums1)