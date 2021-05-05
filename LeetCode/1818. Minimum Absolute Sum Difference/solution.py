class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted(nums1)
        total = sum(abs(x1-x2) for x1, x2 in zip(nums1,nums2))
        if total == 0:
            return 0
        ans = total
        n = len(nums1)
        for x1, x2 in zip(nums1,nums2):
            idx = bisect.bisect_left(arr,x2)
            if idx < n:
                ans = min(ans, total-abs(x1-x2)+abs(arr[idx]-x2))
            if idx-1 >= 0:
                ans = min(ans, total-abs(x1-x2)+abs(arr[idx-1]-x2))
        return ans%(10**9+7)