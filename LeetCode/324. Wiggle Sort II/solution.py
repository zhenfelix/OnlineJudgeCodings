import random
from random import shuffle

class Solution:
    # def kthElement(self, nums, k):
    #     n = len(nums)
    #     print(n)
    #     left, right = -1, 0
    #     while right < n:
    #         if nums[right] >= nums[-1]:
    #             left += 1
    #             nums[left], nums[right] = nums[right], nums[left]
    #         right += 1
    #     if k == left+1:
    #         return nums[left]
    #     elif k < left+1:
    #         return self.kthElement(nums[:left], k)
    #     else:
    #         return self.kthElement(nums[left+1:], k-left-1)
    # cannot pass the last test case multiple [1,2,3]

    def kthElement(self, nums, k):
        n = len(nums)
        left, right, cur = -1, n-1, 0
        while cur < right:
            if nums[cur] > nums[-1]:
                left += 1
                nums[left], nums[cur] = nums[cur], nums[left]
                cur += 1
            elif nums[cur] < nums[-1]:
                right -= 1
                nums[cur], nums[right] = nums[right], nums[cur]
            else:
                cur += 1
        nums[right], nums[n-1] = nums[n-1], nums[right]
        right += 1

        if k > left+1 and k <= right:
            return nums[k-1]
        elif k <= left+1:
            return self.kthElement(nums[:left+1], k)
        else:
            return self.kthElement(nums[right:], k-right)
    
            
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # for i in range(n):
        #     j = random.randint(0,i)
        #     nums[i], nums[j] = nums[j], nums[i]
        shuffle(nums)
            
        mid = self.kthElement(nums, (n+1)//2)
        # print(nums)
        # print(mid)
        def idx(x):
            return (1+x*2)%(n|1)
            
        left, right, cur = -1, n, 0
        while cur < right:
            if nums[idx(cur)] > mid:
                left += 1
                nums[idx(left)], nums[idx(cur)] = nums[idx(cur)], nums[idx(left)]
                cur += 1
            elif nums[idx(cur)] < mid:
                right -= 1
                nums[idx(cur)], nums[idx(right)] = nums[idx(right)], nums[idx(cur)]
            else:
                cur += 1
        return 