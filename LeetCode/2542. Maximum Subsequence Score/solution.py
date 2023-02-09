class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        arr = [(-y,x) for x, y in zip(nums1,nums2)]
        hq = []
        s = 0
        ans = 0
        for y, x in sorted(arr):
            s += x 
            heappush(hq,x)
            if len(hq) > k:
                x = heappop(hq)
                s -= x  
            if len(hq) == k:
                ans = max(ans, s*(-y))
        return ans 
