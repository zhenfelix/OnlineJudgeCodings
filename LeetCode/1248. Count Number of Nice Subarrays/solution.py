class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def lessThanK(target):
            cnt, res = 0, 0
            n = len(nums)
            left = 0
            for right in range(n):
                if nums[right]%2:
                    cnt += 1
                while cnt > target:
                    if nums[left]%2:
                        cnt -= 1
                    left += 1
                res += right-left+1
            return res
        return lessThanK(k)-lessThanK(k-1)



