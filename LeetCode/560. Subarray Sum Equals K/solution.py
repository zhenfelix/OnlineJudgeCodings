class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        sums, ans = 0, 0
        for x in nums:
            sums += x
            if sums-k in mp:
                ans += mp[sums-k]
                
            if sums not in mp:
                mp[sums] = 1
            else:
                mp[sums] += 1
        return ans