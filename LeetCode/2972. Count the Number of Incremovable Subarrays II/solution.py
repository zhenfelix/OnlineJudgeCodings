class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        r = n-2
        while r >= 0 and nums[r] < nums[r+1]:
            r -= 1
        r += 1
        i = 0
        nums.append(inf)
        nums.append(-inf)
        for j in range(r,n+1):
            while i < j and nums[i] > nums[i-1] and nums[i] < nums[j]:
                i += 1
            # print(j,i)
            ans += (i if i == j else i+1)
        # if i < n:
        #     ans += i 
        return ans 