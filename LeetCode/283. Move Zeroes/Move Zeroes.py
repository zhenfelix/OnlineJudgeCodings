class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = 0
        length = len(nums)
        while a < len(nums):
            while nums != [] and nums[a] == 0:
                nums[a: a+1] = []
                if a >= len(nums):
                    break
            a += 1
        nums += [0]*(length-len(nums))


if __name__ == "__main__":
    a = [0,0,1,2,0,4]
    Solution().moveZeroes(a)
    print(a)
