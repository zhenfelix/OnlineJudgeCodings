class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans, cur = 0, 0
        cc = Counter()
        cc[0] += 1
        for a in nums:
            cur ^= a 
            ans += cc[cur]
            cc[cur] += 1
        return ans 