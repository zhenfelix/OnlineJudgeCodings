class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n 
        mx = 0
        for i, a in enumerate(nums):
            mx = max(mx,a)
            ans[i] = a+mx
        cur = 0
        for i in range(n):
            ans[i] += cur 
            cur = ans[i]
        return ans