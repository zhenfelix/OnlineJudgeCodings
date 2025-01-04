class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = nxt = ans = 0
        n = len(nums)
        for i in range(n):
            if i > cur:
                ans += 1
                cur = nxt
            nxt = max(nxt,i+nums[i])
        return ans