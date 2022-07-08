class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        presums1, presums2 = [0], [0]
        for i in range(n):
            presums1.append(presums1[-1]+nums1[i])
            presums2.append(presums2[-1]+nums2[i])
        ans = max(presums1[-1],presums2[-1])
        mi, mx = float('inf'), -float('inf')
        for j in range(n):
            a = presums2[-1]-(presums2[j+1]-presums1[j+1])
            b = presums1[-1]-(presums1[j+1]-presums2[j+1])
            mi = min(mi, presums2[j]-presums1[j])
            mx = max(mx, presums2[j]-presums1[j])
            ans = max(ans, max(a+mx,b-mi))
        return ans



class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        cmx, cmi = 0, 0
        sa, sb = sum(nums1), sum(nums2)
        ans = max(sa, sb)
        for a, b in zip(nums1,nums2):
            cmx = max(0,cmx)+b-a
            cmi = min(0,cmi)+b-a            
            ans = max(ans, max(sa+cmx, sb-cmi))
        return ans


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        ca, cb = 0, 0
        sa, sb = sum(nums1), sum(nums2)
        ans = max(sa, sb)
        for a, b in zip(nums1,nums2):
            ca = max(0,ca)+b-a
            cb = max(0,cb)+a-b            
            ans = max(ans, max(sa+ca, sb+cb))
        return ans 