class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n < 7:
            return False
        for j in range(3,n-3):
            cnt = Counter()
            lo, hi = nums[0], sum(nums[2:j])
            for i in range(1,j-1):
                if lo == hi:
                    cnt[lo] += 1
                lo += nums[i]
                hi -= nums[i+1]
            lo, hi = nums[j+1], sum(nums[j+3:])
            for k in range(j+2,n-1):
                if lo == hi and cnt[lo] > 0:
                    return True
                lo += nums[k]
                hi -= nums[k+1]
        return False