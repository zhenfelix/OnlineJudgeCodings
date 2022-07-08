class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for a in nums:
            ans |= a 
        return ans