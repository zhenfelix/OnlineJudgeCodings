class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, 10**9
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = sum((x-1)//mid for x in nums)
            if cnt <= maxOperations:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo 