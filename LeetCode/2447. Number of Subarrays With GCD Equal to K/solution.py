class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        for i in range(n):
            g = nums[i]
            for j in range(i,n):
                g = gcd(g, nums[j])
                if g == k:
                    res += 1

        return res 