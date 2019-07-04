# https://windliang.cc/2018/07/18/leetCode-4-Median-of-Two-Sorted-Arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kthElement(a, b, k):#start from 0
            if len(a) > len(b):
                a, b = b, a
            if len(a) == 0:
                return b[k-1]
            if k == 1:
                if a[0] <= b[0]:
                    return a[0]
                else:
                    return b[0]
            a_idx, b_idx = min(len(a)-1,k//2-1), k//2-1
            if a[a_idx] <= b[b_idx]:
                return kthElement(a[a_idx+1:],b,k-a_idx-1)
            else:
                return kthElement(a,b[b_idx+1:],k-b_idx-1)
        m, n =len(nums1), len(nums2)
        
        # print(kthElement(nums1, nums2, (m+n+1)//2))
        # print(kthElement(nums1, nums2, (m+n+2)//2))
    
        return (kthElement(nums1, nums2, (m+n+1)//2)+kthElement(nums1, nums2, (m+n+2)//2))/2.0