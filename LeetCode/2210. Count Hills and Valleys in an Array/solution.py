# class Solution:
#     def countHillValley(self, nums: List[int]) -> int:
#         st = []
#         cnt = 0
#         for x in nums:
#             if st and st[-1] == x:
#                 st.pop()
#             elif len(st) > 1 and st[-1] < x and st[-1] < st[-2]:
#                 cnt += 1
#             elif len(st) > 1 and st[-1] > x and st[-1] > st[-2]:
#                 cnt += 1
#             st.append(x)
#         return cnt


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        left = 0
        for i in range(1,n-1):
            if nums[i] == nums[i+1]:
                continue
            if (nums[left] < nums[i] and nums[i] > nums[i+1]) or (nums[left] > nums[i] and nums[i] < nums[i+1]):
                cnt += 1
                # print(left,i,i+1)
            left = i 
        return cnt