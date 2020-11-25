class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        x = sum(nums) - x
        mp = {0: -1}
        cur, res = 0, -float('inf')
        for i, a in enumerate(nums):
            cur += a
            mp[cur] = i 
            if cur - x in mp:
                res = max(res, i-mp[cur-x])
        res = n - res
        return res if res < float('inf') else -1

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left, right = 0, 0
        cur, res = sum(nums), float('inf')
        for right in range(n+1):
            while cur < x and left < right:
                cur += nums[left]
                left += 1
            if cur == x:
                res = min(res,n-(right-left))
            if right == n:
                break
            cur -= nums[right]
        return res if res < float('inf') else -1