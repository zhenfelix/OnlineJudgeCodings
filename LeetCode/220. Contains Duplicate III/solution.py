# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         for i, num in enumerate(nums):
#             for j in range(max(0,i-k),i):
#                 if abs(num-nums[j]) <= t:
#                     return True

#         return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k <= 0 or t < 0:
            return False
        # anchor = min(nums)
        # nums = [num-min(nums) for num in nums]
        # nums = [num-anchor for num in nums]
        bucket = {}
        for i, num in enumerate(nums):
            # bid = (num-anchor)//(t+1)
            bid = num//(t+1)
            if bid in bucket or (bid+1 in bucket and bucket[bid+1]-num <= t) or (bid-1 in bucket and num-bucket[bid-1] <= t):
                return True
            if len(bucket) >= k:
                # last = (nums[i-k]-anchor)//(t+1)
                last = nums[i-k]//(t+1)
                del bucket[last]
            bucket[bid] = num
        return False


