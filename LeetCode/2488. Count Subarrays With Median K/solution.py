class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idx = -1
        for i in range(n):
            if nums[i] == k:
                idx = i 
                break 
        lo, hi = 0, 0 
        cc = Counter()
        cc[0] += 1
        for i in range(idx)[::-1]:
            if nums[i] < k:
                lo += 1
            else:
                hi += 1
            cc[hi-lo] += 1
        ans = 0
        lo, hi = 0, 0
        for i in range(idx,n):
            if nums[i] < k:
                lo += 1
            elif nums[i] > k:
                hi += 1
            ans += cc[lo-hi]
            ans += cc[lo+1-hi]
        return ans 
