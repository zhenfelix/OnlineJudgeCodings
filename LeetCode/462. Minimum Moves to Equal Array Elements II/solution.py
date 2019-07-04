# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         n = len(nums)
#         mid = nums[n//2]
#         ans = 0
#         for num in nums:
#             ans += abs(num-mid)
#         return ans


from random import shuffle


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def kthElement(left, right, k):
            if left == right: return nums[left]
            pivot, i = nums[right], left
            for j in range(left,right):
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if k-1 == i-left:
                return nums[i]
            elif k-1 >i-left:
                return kthElement(i+1, right, k-1-i+left)
            else:
                return kthElement(left,i-1,k)
        
        
        # nums = sorted(nums)
        shuffle(nums)#an sorted array will cost O(n^2) time
        n = len(nums)
        # mid = nums[n//2]
        mid = kthElement(0,n-1,n//2+1)
        ans = 0
        for num in nums:
            ans += abs(num-mid)
        return ans