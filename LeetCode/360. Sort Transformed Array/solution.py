class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = list(map(lambda x: a*x*x+b*x+c, nums))
        if a == 0:
            if b >= 0:
                return nums
            return nums[::-1]
        if a < 0:
            nums = [-x for x in nums]
        idx, Min = 0, float('inf')
        while idx < len(nums) and nums[idx] <= Min:
            Min = nums[idx]
            idx += 1
        res = []
        i, j = idx-1, idx
        # print(nums)
        # print(Min)
        while i >= 0 and j < len(nums):
            if nums[i] < nums[j]:
                res.append(nums[i])
                i -= 1
            else:
                res.append(nums[j])
                j += 1
        while i >= 0:
            res.append(nums[i])
            i -= 1
        while j < len(nums):
            res.append(nums[j])
            j += 1
        if a > 0:
            return res
        return [-x for x in res[::-1]]