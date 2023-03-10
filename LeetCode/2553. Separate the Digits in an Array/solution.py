class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for s in nums:
            for ch in str(s):
                ans.append(int(ch))
        return ans 
