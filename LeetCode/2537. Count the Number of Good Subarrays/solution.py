class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, cnt, cc = 0, 0, Counter()
        n = len(nums)
        ans = 0
        for right in range(n):
            x = nums[right]
            cnt += cc[x]
            cc[x] += 1
            while cnt >= k:
                y = nums[left]
                left += 1
                cc[y] -= 1
                cnt -= cc[y]
            ans += left
        return ans 