class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mx = 32
        pos = [n]*mx
        ans = [0]*n
        for i in range(n)[::-1]:
            v = nums[i]
            p = i
            for j in range(mx)[::-1]:
                bit = (v>>j)&1
                if bit:
                    pos[j] = i  
                elif pos[j] < n:
                    p = max(p, pos[j])
            ans[i] = p-i+1
        return ans