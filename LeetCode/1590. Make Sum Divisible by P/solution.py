class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mp, n = {0: -1}, len(nums)
        cur, res = 0, n
        total = sum(nums)%p
        # print(total)
        if total == 0:
            return 0
        for i, num in enumerate(nums):
            cur += num
            cur %= p
            tmp = cur - total
            tmp %= p
            if tmp in mp:
                res = min(res, i-mp[tmp])
            mp[cur] = i 
        # print(res)
        return -1 if res == n else res 