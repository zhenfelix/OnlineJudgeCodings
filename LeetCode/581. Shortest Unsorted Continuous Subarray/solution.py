# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         left, right = 0, len(nums)-1
#         while left <= right and nums[left] == sorted_nums[left]:
#             left += 1
#         while left <= right and nums[right] == sorted_nums[right]:
#             right -= 1
#         return right-left+1

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        return 0 if right == -1 else right - left + 1


作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/zui-duan-wu-xu-lian-xu-zi-shu-zu-by-leet-yhlf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         mi, mx, n = float('inf'), -float('inf'), len(nums)
#         for i in range(n-1):
#             if nums[i+1] < nums[i]:
#                 mx = max(mx, nums[i])
#                 mi = min(mi, nums[i+1])
#         left, right = 0, n-1
#         while left <= right and nums[left] <= mi:
#             left += 1
#         while left <= right and nums[right] >= mx:
#             right -= 1
#         # print(mi,mx)
#         # print(left, right)
#         return max(0,right-left+1)