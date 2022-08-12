class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0]*2  
        cc = Counter(nums)
        for k, v in cc.items():
            ans[0] += (v//2)
            ans[1] += (v%2)
        return ans