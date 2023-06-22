class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = inf
        cur = nums[:]
        for delta in range(n):
            s = 0
            for i in range(n):
                cur[i] = min(cur[i],nums[(i+delta)%n])
                s += cur[i]
            ans = min(ans,s+x*delta)

        return ans 