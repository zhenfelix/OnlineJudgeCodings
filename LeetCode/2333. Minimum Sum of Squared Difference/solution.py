class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        tot = 0
        k = k1+k2
        diff = []
        ans = 0
        for a, b in zip(nums1,nums2):
            d = abs(a-b)
            diff.append(d)
            tot += d
            ans += d*d 
        if tot <= k:
            return 0
        cur = 0
        cur2 = 0
        n = len(diff)
        diff.sort()
        for i, d in enumerate(diff):
            if k >= tot-cur-d*(n-i):
                plus = k-(tot-cur-d*(n-i))
                d -= plus//(n-i)
                r = plus%(n-i)
                cur2 += d*d*(n-i-r)+(d-1)*(d-1)*r
                return cur2
            cur += d 
            cur2 += d*d 
        return ans