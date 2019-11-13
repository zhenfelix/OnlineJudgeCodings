class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [-float('inf')]+nums+[float('inf')]
        n, isFound = len(nums), False
        for i in range(1,n):
            if nums[i-1] <= nums[i]:
                continue
            elif isFound:
                return False
            else:
                left, right = i-2, i+1
                if nums[left] > nums[right]:
                    return False
                elif nums[i-1] > nums[right] and nums[i] < nums[left]:
                    return False
                else:
                    isFound = True
        return True
