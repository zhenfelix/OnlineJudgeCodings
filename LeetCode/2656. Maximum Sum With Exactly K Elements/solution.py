class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        return (mx+mx+k-1)*k//2